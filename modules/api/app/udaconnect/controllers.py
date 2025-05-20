from datetime import datetime

from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.schemas import (
    ConnectionSchema,
    LocationSchema,
    PersonSchema,
)
from app.udaconnect.services import ConnectionService, LocationService, PersonService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

import requests

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa



@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
#    @responds(schema=PersonSchema)
#    def post(self) -> Person:
#        payload = request.get_json()
#        new_person: Person = PersonService.create(payload)
#        return new_person

    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        r = requests.get("udaconnect-data-api.default.svc.cluster.local:30002/api/persons")
        #persons: List[Person] = {person.id: person for person in r.json()}
        rlist = json.loads(r.json())
        persons = []
        for p in rlist:
            new_person = Person()
            new_person.id = p["id"]
            new_person.first_name = p["first_name"]
            new_person.last_name = p["last_name"]
            new_person.company_name = p["company_name"]
            persons.append(new_person)   
            
        #persons = list(map(lambda x: Person(x[0], x[1], x[2], x[3]), rlist)

        #persons: List[Person] = PersonService.retrieve_all()
        return persons


@api.route("/persons/<person_id>/connection")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        start_date: datetime = datetime.strptime(
            request.args["start_date"], DATE_FORMAT
        )
        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)

        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )
        return results

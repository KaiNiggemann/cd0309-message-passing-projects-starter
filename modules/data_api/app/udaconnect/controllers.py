from datetime import datetime

import json
from kafka import KafkaProducer
from app.udaconnect.models import Location, Person #Connection
from app.udaconnect.schemas import (
    #ConnectionSchema,
    LocationSchema,
    PersonSchema,
)
from app.udaconnect.services import LocationService, PersonService #ConnectionService
from flask import jsonify, request, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect DATA API", description="Connections via geolocation.")  # noqa


@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        KAFKA_SERVER = 'kafka-broker.default.svc.cluster.local:9092'
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
        
        kafka_data = json.dumps( request.get_json() ).encode()
        producer.send("locations", kafka_data )
        print( "Published to {} => {}".format("locations", kafka_data ) )
        return "Published to {} => {}".format("locations", kafka_data )

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location


@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        KAFKA_SERVER = 'kafka-broker.default.svc.cluster.local:9092'
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
        
        kafka_data = json.dumps( request.get_json() ).encode()
        producer.send("persons", kafka_data )
        print ( "Published to {} => {}".format("persons", kafka_data ) )
        return "Published to {} => {}".format("persons", kafka_data )
        
    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        persons: List[Person] = PersonService.retrieve_all()
        return persons


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return person


#@api.route("/persons/<person_id>/connection")
#@api.param("start_date", "Lower bound of date range", _in="query")
#@api.param("end_date", "Upper bound of date range", _in="query")
#@api.param("distance", "Proximity to a given user in meters", _in="query")
#class ConnectionDataResource(Resource):
#    @responds(schema=ConnectionSchema, many=True)
#    def get(self, person_id) -> ConnectionSchema:
#        start_date: datetime = datetime.strptime(
#            request.args["start_date"], DATE_FORMAT
#        )
#        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
#        distance: Optional[int] = request.args.get("distance", 5)
#
#        results = ConnectionService.find_contacts(
#            person_id=person_id,
#            start_date=start_date,
#            end_date=end_date,
#            meters=distance,
#        )
#        return results

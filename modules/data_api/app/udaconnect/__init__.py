from app.udaconnect.models import Location, Person  # Connection
from app.udaconnect.schemas import LocationSchema, PersonSchema  # ConnectionSchema


def register_routes(api, app, root="api"):
    from app.udaconnect.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")

import os
from concurrent import futures

import grpc
import person_pb2
import person_pb2_grpc

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")


class PersonServicer(person_pb2_grpc.PersonServiceServicer):
    def Get(self, request, context):
        Person = PersonService.retrieve(request.id)

        PersonM = person_pb2.PersonResponseMessage(
            id = Person.id,
            first_name = Person.first_name,
            last_name = Person.last_name,
            company_name = Person.company_name,
        )
        return PersonM


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)


if __name__ == "__main__":
    print("Server starting on port 5005...")
    server.add_insecure_port("[::]:5005")
    server.start()
    print("started")
    
    app.run(debug=True, host="0.0.0.0", port=5001)

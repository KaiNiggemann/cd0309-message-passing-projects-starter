import os
from concurrent import futures

import grpc
import person_pb2
import person_pb2_grpc

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")


class PersonServicer(order_pb2_grpc.PersonServiceServicer):
    def Get(self, request, context):
        first_order = order_pb2.OrderMessage(
            id="2222",
            created_by="USER123",
            status=order_pb2.OrderMessage.Status.QUEUED,
            created_at='2020-03-12',
            equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
        )

        result = order_pb2.OrderMessageList()
        result.orders.extend([first_order, second_order])
        return result

    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "created_by": request.created_by,
            "status": request.status,
            "created_at": request.created_at,
            "equipment": ["KEYBOARD"]
        }
        print(request_value)

        return order_pb2.OrderMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)


if __name__ == "__main__":
    print("Server starting on port 5005...")
    server.add_insecure_port("[::]:5005")
    server.start()
    print("started")
    
    app.run(debug=True)

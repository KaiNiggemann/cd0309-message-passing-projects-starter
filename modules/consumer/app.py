import json
import threading
from services import LocationService, PersonService #ConnectionService
import asyncio
from kafka import KafkaConsumer


def consumer1(self):
  print("Start consuming 'locations'...")
  consumer = KafkaConsumer('locations')
  for message in consumer:
    try:
      print ("Location:" + str(json.loads(message.value.decode('ascii')) ))
    except:
      print("This seems not a valid JSON format with double quotes")

def consumer2(self):
  print("Start consuming 'persons'...")
  consumer = KafkaConsumer('locations')
  for message in consumer:
    try:
      print ("Person:" + str( json.loads(message.value.decode('ascii')) ))
    except:
      print("This seems not a valid JSON format with double quotes")


if __name__ == '__main__':
    consumer1_thread = threading.Thread(target=consumer1, args=())
    consumer2_thread = threading.Thread(target=consumer2, args=())
    consumer1_thread.daemon = True
    consumer2_thread.daemon = True
    consumer1_thread.start()
    consumer2_thread.start()


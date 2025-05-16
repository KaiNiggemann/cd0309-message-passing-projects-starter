import json
import os
import threading
from services import LocationService, PersonService #ConnectionService

from flask_kafka import FlaskKafka
from kafka import KafkaConsumer
from app import create_app


app = create_app(os.getenv("FLASK_ENV") or "test")
#bus = FlaskKafka()
#bus.init_app(app)

#@bus.handle('locations')
def test_topic_handler(consumer, msg):
  print("Start consuming 'locations'...")
  try:
    content = json.loads(msg.value.decode('ascii'))
  except:
    print("This seems not a valid JSON format with double quotes")
    return
  
  print ("Location - processing message: " + str(content))
  Location = LocationService.create(content)
  print (Location)
  return
  
#@bus.handle('persons')
def test_topic_handler(consumer,msg):
  print("Start consuming 'persons'...")
  try:
    content = json.loads(msg.value.decode('ascii'))
  except:
    print("This seems not a valid JSON format with double quotes")
    return
      
  print ("Person - processing message: " + str(content))
  Person = PersonService.create(content)
  print (Person)
  return


def consumer1():
  print("Start consuming 'locations'...")
  consumer = KafkaConsumer('locations', bootstrap_servers='kafka-broker.default.svc.cluster.local:9092')
  for message in consumer:
    try:
      content = json.loads(message.value.decode('ascii'))
    except:
      print("This seems not a valid JSON format with double quotes")

    print ("Location - processing message: " + str(content))
    Location = LocationService.create(content)
    print (Location)

  return

def consumer2():
  print("Start consuming 'persons'...")
  consumer = KafkaConsumer('persons', bootstrap_servers='kafka-broker.default.svc.cluster.local:9092')
  for message in consumer:
    try:
      content = json.loads(message.value.decode('ascii'))
    except:
      print("This seems not a valid JSON format with double quotes")

    print ("Person - processing message: " + str(content))
    Person = PersonService.create(content)
    print (Person)

  return


if __name__ == '__main__':
    consumer1_thread = threading.Thread(target=consumer1)
    consumer2_thread = threading.Thread(target=consumer2)
    consumer1_thread.start()
    consumer2_thread.start()
    app.run(debug=True)


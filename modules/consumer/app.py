import json
#import threading
import os
from services import LocationService, PersonService #ConnectionService
#import asyncio
#from kafka import KafkaConsumer
from flask_kafka import FlaskKafka
from app import create_app


app = create_app(os.getenv("FLASK_ENV") or "test")
bus = FlaskKafka()
bus.init_app(app)

@bus.handle('locations')
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
  
@bus.handle('persons')
def test_topic_handler(consumer,msg):
  print("Start consuming 'persons'...")
  try:
    content = json.loads(message.value.decode('ascii'))
  except:
    print("This seems not a valid JSON format with double quotes")
    return
      
  print ("Person - processing message: " + str(content))
  Person = PersonService.create(content)
  print (Person)
  return


if __name__ == '__main__':
  bus.run()
  app.run(debug=True)

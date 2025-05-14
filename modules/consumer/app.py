import json
from services import LocationService, PersonService #ConnectionService
import asyncio
from kafka import KafkaConsumer

TOPIC_NAME = 'locations'


if __name__ == '__main__':
  consumer = KafkaConsumer(TOPIC_NAME, value_deserializer=lambda m: json.loads(m.decode('ascii')))
  for message in consumer:
    try:
      print (message.value)
    except:
      print("This seems not a valid JSON format with double quotes")

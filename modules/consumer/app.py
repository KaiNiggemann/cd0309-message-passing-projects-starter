import json
from services import LocationService, PersonService #ConnectionService
import asyncio
from kafka import KafkaConsumer

TOPIC_NAME = 'locations'


if __name__ == '__main__':
  consumer = KafkaConsumer(TOPIC_NAME)
  for message in consumer:
    print (message.value)

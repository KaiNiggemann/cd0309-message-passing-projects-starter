import json
from services import retrieve_orders, create_order

from kafka import KafkaConsumer

TOPIC_NAME = 'locations'


if __name__ == '__main__':
  consumer = KafkaConsumer(TOPIC_NAME)
  for message in consumer:
    print (message)

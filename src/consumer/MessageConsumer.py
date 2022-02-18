import json

from kafka import KafkaConsumer

from Neo4j import Neo4j

TOPIC_NAME = 'clickstream'

consumer = KafkaConsumer(TOPIC_NAME)

for message in consumer:
    print(message)
    arr = json.loads(message.value)
    Neo4j.hanldeGraph(arr)

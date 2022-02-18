import json

from kafka import KafkaProducer


class MessageProducer:
    TOPIC_NAME = 'clickstream'
    KAFKA_SERVER = 'localhost:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, value_serializer=lambda v: json.dumps(v, indent=4, sort_keys=True, default=str).encode('utf-8'))

    @staticmethod
    def sendMessage(message):
        MessageProducer.producer.send(MessageProducer.TOPIC_NAME, message)
        MessageProducer.producer.flush()



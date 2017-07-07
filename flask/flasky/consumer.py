# coding: utf-8
from kafka import KafkaConsumer
consumer = KafkaConsumer('test',bootstrap_servers=['11.205.240.93:9092'])
for msg in consumer:
	print((msg.value).decode('utf8'))

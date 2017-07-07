# coding:utf-8
import time
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='11.205.240.93:9092')
while True:
	producer.send('test', "Hello World!".encode('utf8'))
	time.sleep(3)
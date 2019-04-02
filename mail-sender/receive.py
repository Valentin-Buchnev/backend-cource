#!/usr/bin/env python
import pika
import traceback, sys

import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from flask import Flask

conn_params = pika.ConnectionParameters('rabbit', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='queue', durable=True)

print("Waiting for messages. To exit press CTRL+C")

def callback(ch, method, properties, body):
    email, confirm_url = body.split(" ")

    msg = MIMEMultipart()
    msg['From'] = 'a.einstein1488@gmail.com'
    msg['To'] = email
    msg['Subject'] = "Verification"
    
    msg.attach(MIMEText(confirm_url, 'plain'))

    try:
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpObj.starttls()
        smtpObj.login('a.einstein1488@gmail.com', 'abacaba_1')
        smtpObj.sendmail('a.einstein1488@gmail.com', 
                email, msg.as_string())
        smtpObj.quit()
        return True
    except Exception:
        return False

channel.basic_consume('queue', callback)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
except Exception:
    channel.stop_consuming()
    traceback.print_exc(file=sys.stdout)

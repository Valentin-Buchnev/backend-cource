#!/usr/bin/env python
import pika
import traceback, sys

import smtplib

conn_params = pika.ConnectionParameters('rabbit', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='queue', durable=True)

print("Waiting for messages. To exit press CTRL+C")

def callback(ch, method, properties, body):
    email, confirm_url = body.split(" ")
    try:
        smtpObj = smtplib.SMTP('smtp.mail.ru', 465)
        smtpObj.starttls()
        smtpObj.login('backend.mipt@bk.ru','lolkek123')
        smtpObj.sendmail("backend.mipt@bk.ru", email, confirm_url)
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


from amqpmanager import MQConnector
import pika
from  amqpmanager import MQSender
class SendException:
    def __init__(self,host="127.0.0.1",port="15672",virtualhost="guest",username="guest",password="guest",queue="TEST"):
        self.host=host
        self.port=port
        self.virtualhost=virtualhost
        self.username=username
        self.password=password
        connector=MQConnector()
        self.connection =pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel=self.connection.channel()
        self.sender=MQSender()
        self.exchange=""
        self.routing_key=queue
    def send_exception(self, exception):
        messageString=exception['message']
        self.sender.send(self.connection,self.channel,self.exchange,self.routing_key,messageString)

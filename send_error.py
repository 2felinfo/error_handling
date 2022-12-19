
from amqpmanager import MQConnector

from  amqpmanager import MQSender
class SendException:
    def __init__(self,host="10.13.2.137",port="5672",virtualhost="CaptosDev",username="CaptosDev",password="CaptosDev",queue="TESTQUEUE"):
        self.host=host
        self.port=port
        self.virtualhost=virtualhost
        self.username=username
        self.password=password
        self.connection=MQConnector.connect_with_credentials(self.host,self.port,self.virtualhost,self.username,self.password)
        self.channel=self.connection.channel()
        self.sender=MQSender()
        self.exchange=""
        self.routing_key=queue

    def send_exception(self):

        self.sender.send(self.connection,self.channel,self.exchange,self.routing_key,"hello")

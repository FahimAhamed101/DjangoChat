from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

from django.contrib.auth.models import User
from datetime  import datetime


class ChatConsumer(WebsocketConsumer):
    
    
        
    def receiver_function(self,the_data_will_come_from_layer):
        data=json.dumps(the_data_will_come_from_layer)
        self.send(data)
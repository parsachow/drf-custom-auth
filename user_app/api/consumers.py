from channels.generic.websocket import AsyncWebsocketConsumer
from channels import layers
import json


# channel_layer = get_channel_layer()

class NotificationConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = 'notification'
        self.room_group_name = self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
  
  
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    
    
    # Receive message from WebSocket
    async def receive(self, text_data):
        
        data = {
            'type': 'send_notification',
            'notification': text_data
        }
        
        #send notification to group
        await self.channel_layer.group_send(self.room_group_name, data)
    
    async def send_notification(self, event):
        
        print(event)
        await self.send(text_data=event['notification'])
       
      
       
    
        
    # set group room name vs group name
    # receiver function
    # send notification function -> view function
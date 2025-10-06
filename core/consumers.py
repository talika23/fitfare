import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "notifications"
        # Join group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        # Optional: send welcome message
        await self.send(json.dumps({"msg": "Connected to FitFare notifications"}))

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Receive message from WebSocket (client -> server)
    async def receive(self, text_data):
        # If clients send messages via WS, optionally broadcast
        data = json.loads(text_data)
        msg = data.get("msg", "")
        # Broadcast to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "send_notification",
                "message": f"User says: {msg}"
            }
        )

    # Receive message from group
    async def send_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'msg': message
        }))

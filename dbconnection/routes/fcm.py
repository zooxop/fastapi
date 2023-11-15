from fastapi import Depends, HTTPException, status, Header, APIRouter
from firebase_admin import auth, messaging

fcm_router = APIRouter()

@fcm_router.post('/send-push-notification')
async def send_push_notification(user_token: str, text: str):
    message = messaging.Message(
        token=user_token,
        notification=messaging.Notification(
            title="새로운 메시지",
            body=text
        )
    )
    response = messaging.send(message)
    return response
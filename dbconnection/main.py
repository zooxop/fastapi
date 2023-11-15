import os
import firebase_admin
from firebase_admin import credentials
from typing import Optional
from fastapi import FastAPI
from routes.test import test_router
from routes.fcm import fcm_router


def initialize_firebase():
    firebase_cred = credentials.Certificate("./path/to/serviceAccountKey.json")
    firebase_admin.initialize_app(firebase_cred)


app = FastAPI() # FastAPI 모듈
app.include_router(test_router) # 다른 route파일들을 불러와 포함시킴
app.include_router(fcm_router, prefix="/fcm") # FCM router add
app.add_event_handler("startup", initialize_firebase)


@app.get("/") # Route Path
def index():
    return {
        "Python": "Framework",
    }
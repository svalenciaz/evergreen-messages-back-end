from fastapi import APIRouter, Response
from starlette.status import HTTP_404_NOT_FOUND
from config.db import db
from models.message import Message
from bson.objectid import ObjectId
from schemas.message import messageEntity, messageEntities

message_router = APIRouter()

@message_router.get('/messages')
async def get_messages():
    return messageEntities(db.messages.find({}))

@message_router.get('/messages/{id}')
async def get_message(id: str):
    message = db.messages.find_one({"_id" : ObjectId(id)})
    if message:
        return messageEntity(message)
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)

@message_router.post('/messages')
async def create_message(message: Message):
    message = dict(message)
    inserted_message_id = db.messages.insert_one(message).inserted_id
    message = db.messages.find_one({"_id": inserted_message_id})
    return messageEntity(message)

@message_router.put('/messages/{id}')
async def update_message(id: str, message: Message):
    updated_message = db.messages.find_one_and_update({"_id" : ObjectId(id)}, {"$set" : dict(message) })
    if updated_message:
        return messageEntity(db.messages.find_one({"_id": updated_message['_id']}))
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)

@message_router.delete('/messages/{id}')
async def delete_message(id):
    deleted = db.messages.find_one_and_delete({"_id" : ObjectId(id)})
    if deleted:
        return messageEntity(deleted)
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)
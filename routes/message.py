from datetime import datetime
from fastapi import APIRouter, Response
from starlette.status import HTTP_404_NOT_FOUND
from config.db import db
from models.message import Message
from bson.objectid import ObjectId
from schemas.message import messageEntity, messageEntities
from schemas.user import userEntities, userEntity
from config.message import create_content, send_message

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

@message_router.post('/messages/send')
async def create_message(message: Message):
    message = dict(message)
    sender = userEntity(db.users.find_one({"_id": ObjectId(message['sender'])}))
    receivers = userEntities(db.users.find({"_id": {"$in" : [ObjectId(receiver_id) for receiver_id in message['receivers']]}}))
    contents = [create_content(user['name'], user['gender'], message["content"]) for user in receivers]
    for user, content in zip(receivers, contents):
        send_message(message['subject'], content, user['email'], sender['email'])
    message['send_date'] = datetime.now()
    message['creation_date'] = datetime.now()
    message['status'] = 'sent'
    inserted_message_id = db.messages.insert_one(message).inserted_id
    message = db.messages.find_one({"_id": inserted_message_id})
    return messageEntity(message)

@message_router.post('/messages/draft')
async def create_message(message: Message):
    message = dict(message)
    message['creation_date'] = datetime.now()
    message['status'] = 'draft'
    inserted_message_id = db.messages.insert_one(message).inserted_id
    message = db.messages.find_one({"_id": inserted_message_id})
    return messageEntity(message)

@message_router.put('/messages/{id}')
async def update_message(id: str):
    changes = {"status": "sent", "send_date": datetime.now()}
    updated_message = db.messages.find_one_and_update({"_id" : ObjectId(id), "status": "draft"}, {"$set" : changes })
    if updated_message:
        sender = userEntity(db.users.find_one({"_id": ObjectId(updated_message['sender'])}))
        receivers = userEntities(db.users.find({"_id": {"$in" : [ObjectId(receiver_id) for receiver_id in updated_message['receivers']]}}))
        contents = [create_content(user['name'], user['gender'], updated_message["content"]) for user in receivers]
        for user, content in zip(receivers, contents):
            send_message(updated_message['subject'], content, user['email'], sender['email'])
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
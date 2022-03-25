from fastapi import APIRouter, Response
from starlette.status import HTTP_404_NOT_FOUND
from ..config.db import db
from ..models.user import User
from bson.objectid import ObjectId
from ..schemas.user import userEntity, userEntities

user_router = APIRouter()

@user_router.get('/users')
async def get_users():
    return userEntities(db.users.find({}))

@user_router.get('/users/senders')
async def get_senders():
    return userEntities(db.users.find({"sender" : True}))

@user_router.get('/users/receivers')
async def get_recievers():
    return userEntities(db.users.find({"receiver" : True}))

@user_router.get('/users/{id}')
async def get_user(id: str):
    user = db.users.find_one({"_id" : ObjectId(id)})
    if user:
        return userEntity(user)
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)

@user_router.post('/users')
async def create_user(user: User):
    user = dict(user)
    inserted_user_id = db.users.insert_one(user).inserted_id
    user = db.users.find_one({"_id": inserted_user_id})
    return userEntity(user)

@user_router.put('/users/{id}')
async def update_user(id: str, user: User):
    updated_user = db.users.find_one_and_update({"_id" : ObjectId(id)}, {"$set" : dict(user) })
    if updated_user:
        return userEntity(db.users.find_one({"_id": updated_user['_id']}))
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)

@user_router.delete('/users/{id}')
async def delete_user(id):
    deleted = db.users.find_one_and_delete({"_id" : ObjectId(id)})
    if deleted:
        return userEntity(deleted)
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)
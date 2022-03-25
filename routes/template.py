from fastapi import APIRouter, Response
from starlette.status import HTTP_404_NOT_FOUND
from ..config.db import db
from ..models.template import Template
from bson.objectid import ObjectId
from ..schemas.template import templateEntity, templateEntities

template_router = APIRouter()

@template_router.get('/templates')
async def get_templates():
    return templateEntities(db.templates.find({}))

@template_router.get('/templates/{id}')
async def get_template(id: str):
    template = db.templates.find_one({"_id" : ObjectId(id)})
    if template:
        return templateEntity(template)
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)

@template_router.post('/templates')
async def create_template(template: Template):
    template = dict(template)
    inserted_template_id = db.templates.insert_one(template).inserted_id
    template = db.templates.find_one({"_id": inserted_template_id})
    return templateEntity(template)

@template_router.put('/templates/{id}')
async def update_template(id: str, template: Template):
    updated_template = db.templates.find_one_and_update({"_id" : ObjectId(id)}, {"$set" : dict(template) })
    if updated_template:
        return templateEntity(db.templates.find_one({"_id": updated_template['_id']}))
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)

@template_router.delete('/templates/{id}')
async def delete_template(id):
    deleted = db.templates.find_one_and_delete({"_id" : ObjectId(id)})
    if deleted:
        return templateEntity(deleted)
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)
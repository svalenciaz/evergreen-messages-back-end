from fastapi import FastAPI
from routes.user import user_router
from routes.template import template_router

app = FastAPI(
    title="Evergreen Back End",
    description= "Backend to control Messages sended by Evergreen",
    version="1.0.1"
    )

app.include_router(user_router)
app.include_router(template_router)
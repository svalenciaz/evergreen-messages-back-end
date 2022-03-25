from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.user import user_router
from .routes.template import template_router
from .routes.message import message_router

app = FastAPI(
    title="Evergreen Back End",
    description= "Backend to control Messages sended by Evergreen",
    version="1.0.1"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)
app.include_router(template_router)
app.include_router(message_router)
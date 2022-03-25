from fastapi import FastAPI
from routes.user import user_router

app = FastAPI(
    title="Evergreen Back End",
    description= "Backend to control Messages sended by Evergreen",
    version="1.0.1"
    )

app.include_router(user_router)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import weather

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(weather.router)
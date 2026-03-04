from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from form_router import form_router

app = FastAPI()
app.include_router(form_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from form_router import form_router

app = FastAPI()
app.include_router(form_router)
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["92.246.76.92", "127.0.0.1:5173"]
)

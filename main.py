from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from form_router import form_router

app = FastAPI()
app.include_router(form_router)
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["admiraltest.ru", "127.0.0.1:5173"]
)

from fastapi import FastAPI
import uvicorn

from form_router import form_router

app = FastAPI()
app.include_router(form_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

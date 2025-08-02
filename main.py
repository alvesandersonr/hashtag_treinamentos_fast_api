from fastapi import FastAPI

app = FastAPI()

from routes.web import web_router

app.include_router(web_router)

# para rodar o nosso codigo execut uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from .db import DAO

class User(BaseModel):
    user: str
    password: str

app = FastAPI()

@app.get("/")
def raiz():
    return RedirectResponse(url='/docs')

@app.get("/user/get_users")
def get_users():
    dao = DAO()
    table = dao.get_users()
    return table

@app.get("/user/get_user/{name}")
def get_user(name: str):
    paramter = (name)
    dao = DAO(paramter)
    table = dao.get_user()
    return table

@app.post('/user/delete_user')
def delete_user(id: int):
    parameter = (id)
    dao = DAO(parameter)
    table = dao.delete_user()
    return table

@app.post(('/user/insert_user'))
def insert_user(model: User):
    parameters = (model.user, model.password)
    dao = DAO(parameters)
    table = dao.insert_user()
    return table
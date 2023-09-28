from fastapi import  Request

# Jinja
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from models.note import Note
from config.db import conn

from schemas.note import noteEntity , notesEntity

note = APIRouter()

# Template
templates =Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request:Request):
    """
    Display main page
    """
    docs =  conn.find()
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
            "important":doc["important"],
        })
    print("documents",newDocs)
    return templates.TemplateResponse("index.html",{"request":request, "newDocs":newDocs})

@note.post("/")
async def create_note(request:Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"]= True if formDict["important"]=="on" else False
    inserted_note = conn.insert_one(formDict)
    return {"Success":True}
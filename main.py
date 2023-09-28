from fastapi import FastAPI, Request
# Jinja
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


app = FastAPI()

# Static files
app.mount("/static",StaticFiles(directory="static"),name="static")


# # Mongo Db connection
# try:
#     # comment:
#     conn = MongoClient("mongodb+srv://rahul:Rahuldubey123@cluster0.uha5oea.mongodb.net/")
#     db   = conn.get_database("Learn")
#     collection = db.get_collection("fastApi") 
 
# except Exception as e:
#     print("Error getting \n\n")
#     raise e
# # end try


# @app.get("/", response_class=HTMLResponse)
# async def read_item(request:Request):
#     """
#     Display main page
#     """
#     docs =  collection.find()
#     newDocs = []
#     for doc in docs:
#         newDocs.append({
#             "id":doc["_id"],
#             "note":doc["note"]
#         })
#     print("documents",newDocs)
#     return templates.TemplateResponse("index.html",{"request":request, "newDocs":newDocs})

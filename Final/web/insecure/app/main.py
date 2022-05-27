from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from tinydb import TinyDB, Query
from pydantic import BaseModel
from hashlib import md5
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
db = TinyDB('db.json')
Insecuritys = Query()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.post("/create")
def create_insecurity(request: Request, insecurity: str = Form(...)):
    row_id = db.insert({"insecure_id":"", "value": insecurity})
    insecure_id = md5(str(row_id).encode("utf-8")).hexdigest()
    db.update({'insecure_id': insecure_id}, doc_ids=[row_id])
    return RedirectResponse(str(request.url)[:-6] + "insecurity/" + insecure_id, status_code=303) 
    
    
@app.get("/insecurity/{insecure_id}")
def read_insecurity(request: Request, insecure_id: str):
    try:
        data = db.search(Insecuritys.insecure_id == insecure_id)[0]
        return templates.TemplateResponse("insecure.html",{"request": request, "insecurity": data["value"]})
    except:
        return templates.TemplateResponse("insecure.html",{"request": request, "insecurity": "Not found !"})
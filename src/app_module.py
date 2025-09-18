from nest.core import PyNestFactory, Module
        
from .app_controller import AppController
from .app_service import AppService
from .contact_controller import ContactController
from .static_controller import StaticController
from .contact_service import ContactService
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


@Module(
    imports=[], 
    controllers=[AppController, ContactController, StaticController], 
    providers=[AppService, ContactService]
)
class AppModule:
    pass


app = PyNestFactory.create(
    AppModule,
    description="NFC Contact Sharing Application",
    title="NFC Contact App",
    version="1.0.0",
    debug=True,
)

http_server = app.get_server()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/nfc/michael/", response_class=HTMLResponse)
def get_michael_contact(request: Request):
    contact_data = {
        "full_name": "Michael Anthony Maxwell",
        "email": "michael.quanbyit.com",
        "phone_number": "+6396 1580 1028",
        "company": "QUANBY Solutions, Inc.",
        "title": "Chief Technology Officer",
        "address": "1862-B Dominga Street Pasay City",
        "base_url": "https://recognitionbe.quanbyit.com"
    }
    return templates.TemplateResponse("contact.html", {"request": request, "contact": contact_data})


from nest.core import PyNestFactory, Module
        
from .app_controller import AppController
from .app_service import AppService
from .contact_controller import ContactController
from .static_controller import StaticController
from .contact_service import ContactService
from fastapi import FastAPI


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

@app.get("/nfc/michael/")
def get_michael_contact():
    return {"name": "Michael Maxwell", "email": "michael.quanbyit.com", "phone": "+6396 1580 1028"}


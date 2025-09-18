from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico")
def favicon():
    return FileResponse("static/favicon.ico")

if __name__ == '__main__':
    uvicorn.run(
        'src.app_module:app',  # Correctly reference the FastAPI instance
        host="0.0.0.0",
        port=5003,  # Updated port to avoid conflicts
        reload=True
    )


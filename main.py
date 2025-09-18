import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'src.app_module:app',  # Correctly reference the FastAPI instance
        host="0.0.0.0",
        port=5003,  # Updated port to avoid conflicts
        reload=True
    )


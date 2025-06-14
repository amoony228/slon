from fastapi import FastAPI, APIRouter
import uvicorn

from routes import translation_router

app = FastAPI()

api_router = APIRouter(prefix="/api")
api_router.include_router(translation_router)
app.include_router(api_router)
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")



    



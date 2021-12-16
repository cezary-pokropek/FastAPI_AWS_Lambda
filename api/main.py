from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Setting the handler, lambda function connection to this handler
handler = Mangum(app=app)
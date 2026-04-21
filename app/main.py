from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Sakha Sport API2"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

@app.post("/say-hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
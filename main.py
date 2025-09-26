from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

@app.get("/")
def main():
    return "Hello World"

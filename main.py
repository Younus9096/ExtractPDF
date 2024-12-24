from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_pdf():
    return {"hello": "world"}
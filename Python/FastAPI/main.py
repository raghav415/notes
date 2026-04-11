from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts = [
    {
        "name": "Raghav"
    },
    {
        "name": "Ram"
    }
]

@app.get("/", response_class=HTMLResponse)
def fun():
    return "<h1>Hi</h1>"

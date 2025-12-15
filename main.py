from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"System": "Kyberno", "Status": "Online", "Location": "Greece"}
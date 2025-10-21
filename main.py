from fastapi import FastAPI

app = FastAPI()

@app.get("/goodPayment")
def success():
    return {"status": "200"}

@app.get("/badPayment")
def success():
    return {"status": "400"}

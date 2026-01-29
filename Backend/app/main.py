from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def home():
    return {"Status": "Success", "message": "Beauty Shop API is running!"}
        
    
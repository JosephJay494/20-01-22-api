from fastapi import FastAPI



app = FastAPI()



@app.get("/")
def server():
    return{'message': "server running well!!!!"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = {
        "Clue Carre - Downtown": {            
            "Mon": 28,
            "Tue": 28,
            "Wed": 28,
            "Thu": 28,
            "Fri": 32,
            "Sat": 32,
            "Sun": 32
        },
        "Clue Carre - Metairie": {            
            "Mon": 21,
            "Tue": 21,
            "Wed": 21,
            "Thu": 21,
            "Fri": 24,
            "Sat": 24,
            "Sun": 24
        }
    }
    return data

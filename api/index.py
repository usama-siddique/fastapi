from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = {
        "Clue Carre - Downtown": {            
            "Mon": 25,
            "Tue": 27,
            "Wed": 28,
            "Thu": 19,
            "Fri": 30,
            "Sat": 28,
            "Sun": 30
        },
        "Clue Carre - Metairie": {            
            "Mon": 21,
            "Tue": 21,
            "Wed": 20,
            "Thu": 13,
            "Fri": 22,
            "Sat": 20,
            "Sun": 20
        }
    }
    return data

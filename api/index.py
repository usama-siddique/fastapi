from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = {
        "Clue Carre - Downtown": {            
            "Mon": 28,
            "Tue": 27,
            "Wed": 28,
            "Thu": 28,
            "Fri": 13,
            "Sat": 28,
            "Sun": 29
        },
        "Clue Carre - Metairie": {            
            "Mon": 21,
            "Tue": 21,
            "Wed": 21,
            "Thu": 21,
            "Fri": 11,
            "Sat": 13,
            "Sun": 23
        }
    }
    return data

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = {
        "Clue Carre - Downtown": {            
            "Mon": 25,
            "Tue": 28,
            "Wed": 28,
            "Thu": 27,
            "Fri": 30,
            "Sat": 29,
            "Sun": 30
        },
        "Clue Carre - Metairie": {            
            "Mon": 21,
            "Tue": 21,
            "Wed": 9,
            "Thu": 18,
            "Fri": 23,
            "Sat": 22,
            "Sun": 22
        }
    }
    return data

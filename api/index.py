from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = {
        "Clue Carre - Downtown": {            
            "Mon": 25,
            "Tue": 24,
            "Wed": 28,
            "Thu": 28,
            "Fri": 31,
            "Sat": 30,
            "Sun": 31
        },
        "Clue Carre - Metairie": {            
            "Mon": 21,
            "Tue": 12,
            "Wed": 9,
            "Thu": 18,
            "Fri": 24,
            "Sat": 22,
            "Sun": 23
        }
    }
    return data

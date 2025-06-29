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
            "Fri": 31,
            "Sat": 30,
            "Sun": 23
        },
        "Clue Carre - Metairie": {            
            "Mon": 21,
            "Tue": 21,
            "Wed": 21,
            "Thu": 20,
            "Fri": 24,
            "Sat": 23,
            "Sun": 9
        }
    }
    return data

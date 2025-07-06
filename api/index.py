from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = {
        "Clue Carre - Downtown": {            
            "Mon": 25,
            "Tue": 27,
            "Wed": 27,
            "Thu": 28,
            "Fri": 31,
            "Sat": 30,
            "Sun": 25
        },
        "Clue Carre - Metairie": {            
            "Mon": 21,
            "Tue": 21,
            "Wed": 20,
            "Thu": 21,
            "Fri": 23,
            "Sat": 20,
            "Sun": 19
        }
    }
    return data

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = {
        "Clue Carre - Downtown": {            
            "Mon": 23,
            "Tue": 27,
            "Wed": 28,
            "Thu": 28,
            "Fri": 31,
            "Sat": 30,
            "Sun": 31
        },
        "Clue Carre - Metairie": {            
            "Mon": 21,
            "Tue": 21,
            "Wed": 9,
            "Thu": 19,
            "Fri": 24,
            "Sat": 23,
            "Sun": 9
        }
    }
    return data

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = {
        "Clue Carre - Downtown": {            
            "Mon": 25,
            "Tue": 27,
            "Wed": 28,
            "Thu": 28,
            "Fri": 30,
            "Sat": 27,
            "Sun": 30
        },
        "Clue Carre - Metairie": {            
            "Mon": 21,
            "Tue": 21,
            "Wed": 20,
            "Thu": 21,
            "Fri": 15,
            "Sat": 19,
            "Sun": 19
        }
    }
    return data

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = {
        "Clue Carre - Downtown": {
            "Sun": 32,
            "Mon": 29,
            "Tue": 28,
            "Wed": 28,
            "Thu": 28,
            "Fri": 32,
            "Sat": 32
        },
        "Clue Carre - Metairie": {
            "Sun": 24,
            "Mon": 21,
            "Tue": 21,
            "Wed": 21,
            "Thu": 21,
            "Fri": 24,
            "Sat": 24
        }
    }
    return data

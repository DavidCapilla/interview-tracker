from fastapi import FastAPI
from dataclasses import dataclass
from datetime import datetime

app = FastAPI()


@app.get("/health")
def read_health() -> dict[str, str]:
    return {"status": "ok"}


# @app.get("/exercise")
# def get_exercise():
#     return Exercise("push ups", 5, 3, 10).volume()
#
#
# @dataclass
# class Exercise:
#     name: str
#     reps: int
#     sets: int
#     weight: float
#
#     def volume(self) -> float | int :
#         return self.reps * self.weight


@dataclass
class Application:
    id: str
    company_name: str
    date: datetime
    position: str


@app.get("/applications")
def read_applications() -> list[Application]:
    return [Application("45", "Google", datetime(2025, 3, 1, 14, 30), "back end"),
    Application("55", "Amazon", datetime(2025, 3, 1, 14, 35), "fullstack")]

# datetime(2025, 3, 1, 14, 30)

# TODO retrieve data from data.json
# TODO POST
# TODO com guardar la info
# TODO SSH keys

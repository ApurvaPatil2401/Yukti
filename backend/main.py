from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

from problems import problems
from validators import *
from llm import generate_hint

app = FastAPI()

validation_tracker = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Yukti Backend Running 🚀"}


@app.get("/problems")
def get_problems():
    return {key: value["description"] for key, value in problems.items()}


@app.post("/ask")
def ask_concept(problem_key: str):
    validation_tracker[problem_key] = 0

    first_step = problems[problem_key]["steps"][0]
    question = random.choice(first_step["questions"])

    return {"question": question}


@app.post("/evaluate")
def evaluate(problem_key: str, user_answer: str):
    problem = problems[problem_key]
    step_index = validation_tracker.get(problem_key, 0)

    step = problem["steps"][step_index]
    validator_name = step["validator"]

    validator_function = globals()[validator_name]
    understood = validator_function(user_answer)

    if understood:
        step_index += 1
        validation_tracker[problem_key] = step_index

        if step_index >= len(problem["steps"]):
            validation_tracker[problem_key] = 0
            return {
                "status": "unlocked",
                "solution": problem["solution"]
            }

        next_step = problem["steps"][step_index]
        question = random.choice(next_step["questions"])

        return {
            "status": "continue",
            "question": question
        }

    else:
        hint = generate_hint(step["concept"], user_answer)
        return {
            "status": "locked",
            "hint": hint
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
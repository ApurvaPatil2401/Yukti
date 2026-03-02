from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from problems import problems
from validators import *
from llm import generate_hint

app = FastAPI()

validation_tracker = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
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
    first_question = problems[problem_key]["steps"][0]["question"]
    return {"question": first_question}


@app.post("/evaluate")
def evaluate(problem_key: str, user_answer: str):
    problem = problems[problem_key]
    step_index = validation_tracker.get(problem_key, 0)

    step = problem["steps"][step_index]
    validator_name = step["validator"]

    # Dynamically call validator function
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

        next_question = problem["steps"][step_index]["question"]

        return {
            "status": "continue",
            "question": next_question
        }

    else:
        hint = generate_hint(problem_key, user_answer)
        return {
            "status": "locked",
            "hint": hint
        }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from problems import problems
from llm import generate_concept_question, evaluate_answer, generate_hint

validation_tracker = {}
app = FastAPI()

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
    problem = problems[problem_key]
    question = generate_concept_question(
        problem["description"],
        problem["concept"]
    )
    return {"question": question}


@app.post("/evaluate")
def evaluate(problem_key: str, user_answer: str):
    problem = problems[problem_key]

    understood = evaluate_answer(problem["concept"], user_answer)

    if problem_key not in validation_tracker:
        validation_tracker[problem_key] = 0

    if understood:
        validation_tracker[problem_key] += 1

        # Require 2 successful validations
        if validation_tracker[problem_key] >= 2:
            validation_tracker[problem_key] = 0
            return {
                "status": "unlocked",
                "solution": problem["solution"]
            }
        else:
            # Ask second question
            second_question = generate_concept_question(
                problem["description"],
                problem["concept"]
            )
            return {
                "status": "continue",
                "question": second_question
            }

    else:
        hint = generate_hint(problem["concept"], user_answer)
        return {
            "status": "locked",
            "hint": hint
        }
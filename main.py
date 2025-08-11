import random

def generate_linear():
    a = random.randint(1, 10)
    x = random.randint(1, 10)
    b = random.randint(1, 10)
    c = a * x + b
    question = f"Solve for x: {a}x + {b} = {c}"
    return question, x

def quiz(num_questions):
    score = 0
    for i in range(num_questions):
        question, answer = generate_linear()
        print(f"Question {i+1}: {question}")
        try:
            user_answer = float(input("Your answer: "))
            if user_answer == answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. Corrct answer was {answer}")
        except ValueError:
            print("Invalid input. Skipping question.\n")
    print(f"Your score {score}/{num_questions} {(score/num_questions) * 100:.2f}%")

quiz(5)
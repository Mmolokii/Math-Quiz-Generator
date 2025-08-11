import random

def generate_linear():
    a = random.randint(1, 10)
    x = random.randint(1, 10)
    b = random.randint(1, 10)
    c = a * x + b
    question = f"Solve for x: {a}x + {b} = {c}"
    return question, x
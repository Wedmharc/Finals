import random

# Step 1: Generate math questions
def generate_math_questions(num_questions=100):
    questions = []
    operations = ['+', '-', '*', '/']
    
    for _ in range(num_questions):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(operations)
        
        if operation == '/':
            # Ensure we don't divide by zero
            while num2 == 0:
                num2 = random.randint(1, 100)
            question = f"{num1} / {num2}"
            answer = round(num1 / num2, 2)  # Keep division answers to 2 decimal places
        elif operation == '+':
            question = f"{num1} + {num2}"
            answer = num1 + num2
        elif operation == '-':
            question = f"{num1} - {num2}"
            answer = num1 - num2
        elif operation == '*':
            question = f"{num1} * {num2}"
            answer = num1 * num2
        
        questions.append({"question": question, "answer": answer})
    
    return questions

# Step 2: Quiz logic
def math_quiz():
    questions = generate_math_questions()
    score = 0
    user_answers = []

    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        user_answer = input("Your answer: ").strip()

        try:
            user_answer = float(user_answer)
            correct_answer = q["answer"]
            if abs(user_answer - correct_answer) < 0.01:  # Allow a small margin for rounding errors
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}")
        except ValueError:
            print(f"Invalid input! The correct answer is {q['answer']}")
        
        user_answers.append({"question": q["question"], "your_answer": user_answer, "correct_answer": q["answer"]})

    # Step 3: Display results
    print("\nQuiz Complete!")
    print(f"Your final score is {score} out of {len(questions)}")

    print("\nSummary of your answers:")
    for i, answer in enumerate(user_answers):
        print(f"Question {i+1}: {answer['question']}")
        print(f"Your answer: {answer['your_answer']}")
        print(f"Correct answer: {answer['correct_answer']}")
        print()

# Run the quiz
if __name__ == "__main__":
    math_quiz()

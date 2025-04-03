import random

def math_quiz():
    score = 0
    for _ in range(5):  # Ask 5 questions
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-'])

        question = f"{num1} {operation} {num2}"
        answer = eval(question)  # Calculate the correct answer
        user_answer = input(f"solve: {question}? ")
        
        if user_answer.isdigit() and int(user_answer) == answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The right answer is {answer}.")

    print(f"🎉 You scored: {score}/5. Well done!")

# Call the function once to start the quiz
math_quiz()
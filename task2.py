import random
import time

print("Let's play!")
time_start = time.time()


def quiz():
    num1 = random.randrange(0, 101)
    num2 = random.randrange(0, 101)
    operator = random.choice(["+", "-"])

    if operator == "+":
        answer_correct = num1 + num2
    elif operator == "-":
        answer_correct = num1 - num2

    text_answer = "{} {} {} = ".format(num1, operator, num2)
    answer_user = int(input(text_answer,))
    while(answer_user != answer_correct):
        text_wrong = "Wrong, try again: " + text_answer
        answer_user = int(input(text_wrong,))


for i in range(10):
    quiz()

time_finish = time.time()
time_spent = int(time_finish - time_start)
mins = int(time_spent / 60)
secs = time_spent % 60
result = "You spent {} minutes and {} seconds".format(mins, secs)
print(result)

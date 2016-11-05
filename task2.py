import sqlite3
import random
import time


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


def game():
    print("Let's play!")
    time_start = time.time()

    for i in range(10):
        quiz()

    time_finish = time.time()
    time_spent = int(time_finish - time_start)
    mins = int(time_spent / 60)
    secs = time_spent % 60
    result = "{} minutes and {} seconds".format(mins, secs)
    print("You spent " + result)
    player_name = input("Enter your name: ", )

    c.execute("INSERT INTO People VALUES (?, ?)", (player_name, result))
    conn.commit()


def show_results():
    c.execute('SELECT * from People')
    if len(c.fetchall()) <= 0:
        print("No results yet")
    for row in c.execute('SELECT * from People'):
        print(row)


conn = sqlite3.connect('leaderboard.db')
c = conn.cursor()
c.execute("CREATE TABLE if not exists People (Name, Result)")

menu_item = 0

while menu_item != 3:
    print("\nHi! This is menu:\n\t1. Start game\n\t2. See results\n\t3. Quit")
    menu_item = int(input("What would you like to do? ", ))

    if menu_item == 1:
        game()

    elif menu_item == 2:
        show_results()

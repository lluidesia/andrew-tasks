print("**********************************")
print("*********** Greetings!************")
print("********* This is task 1 *********")
print("**********************************")
print()
print("What is the average sleeping time that you slept during last year?")

sleep_average = float(input())

while(sleep_average <= 0):
    sleep_average = float(input("This is strange, try again: ", ))

sleep_dif = (sleep_average - 8) * 365 / 24
print("Your differens with normal sleep time is {:.1f} days a year.".format(
    sleep_dif))

if sleep_dif == 0:
    print("You are normal human, live long and prosper!")
elif sleep_dif < 0:
    print("What a hell are you doing?Don't you want to live long and prosper?")
elif sleep_dif > 0:
    print("You like to sleep Lazy Ass, aren't you?")

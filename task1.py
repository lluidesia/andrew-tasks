print("*"*47)
print("*"*3+" "*15+"Greetings!"+" "*16+"*"*3)
print("*"*3+" "*4+"Just a test app that prints title"+" "*4+"*"*3)
print("*"*47)
print()
print("What is the average sleeping time that you slept during last year?")

sleep_average = float(input())

while(sleep_average<=0):
	sleep_average = float(input("This is strange, try again: ", ))

sleep_difference=(sleep_average-8)*365/24

if sleep_difference==0:
	print("Your sleep differens with normal sleep time is %.1f days a year." %sleep_difference)
	print("You are normal human, live long and prosper!")
elif sleep_difference<0:
	print("Your sleep differens with normal sleep time is %.1f days a year." %sleep_difference)
	print("What a hell are you doing? Don't you want to live long and prosper?")
elif sleep_difference>0:
	print("Your sleep differens with normal sleep time is %.1f days a year." %sleep_difference)
	print("You like to sleep Lazy Ass, aren't you?")

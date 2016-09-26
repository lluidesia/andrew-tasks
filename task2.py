import random
import time

print("Let's play!")
time_start=time.time()

for i in range(10):
	num1=random.randrange(0, 101)
	num2=random.randrange(0, 101)
	operator=random.choice(["+", "-"])

	if operator=="+":
		answer_correct=num1+num2
	elif operator=="-":
		answer_correct=num1-num2

	answer_user=int(input(str(num1)+operator+str(num2)+'=',))
	while(answer_user!=answer_correct):
		answer_user=int(input("Wrong, try again: "+str(num1)+operator+str(num2)+'=',))

time_finish=time.time()
time_spent=int(time_finish-time_start)
mins=int(time_spent/60)
secs=time_spent%60

print("You spent "+str(mins)+" minutes and "+str(secs)+" seconds")

import random
print("Hello, I am going to try to guess your age.")
name = input("What is your name?")
print("Welcome" + name)

while True:
	age_guess = random.randint(15,30)
	answer = input(f"Is your age {age_guess}? (y/n): ").lower()

	if answer == 'y':
		print(f"Hooray! {name} is {age_guess} years old. ")
		break

	else:
		print("Dang it, I will try again")


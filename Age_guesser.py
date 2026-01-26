import random
print("Hello, I am going to try to guess your age.")
name = input("What is your name? ")
print("Welcome" + name)

ages = list(range(15,31))

while ages:
	age_guess = random.choice(ages)
	answer = input(
	f"Is your age {age_guess}? (y = yes, o = older, u = younger): " ).lower()


	if answer == 'y':
		print(f"Hooray! {name} is {age_guess} years old.")
		break


	elif answer == 'o':
		ages = [age for age in ages if age > age_guess]
		print("Dang it, I'll guess older.")


	elif answer == 'u': 
		ages = [age for age in ages if age < age_guess]
		print("Dang it, I'll guess younger.")


	else:
		print("Please enter y, o, or u.")


else:
	print("Hmm... something doesn't add up!")

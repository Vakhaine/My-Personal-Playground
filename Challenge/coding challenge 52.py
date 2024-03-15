import random

first_prompt = int(input("Enter the lower bound: "))
second_prompt = int(input("Enter the upper bound: "))

random_number = random.randrange(first_prompt, second_prompt)

print(random_number)
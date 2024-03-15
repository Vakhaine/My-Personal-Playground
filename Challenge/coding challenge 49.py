import json

with open("../Challenge/Questions.json", "r") as file:
    content = file.read()
# print(type(content))
data = json.loads(content)
# print(type(data))

for question in data:
    print(question["Question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["Correct_Answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = (f"{index + 1}  {result} - Your answer: {question['user_choice']}, "
               f"Correct answer: {question['Correct_Answer']}")
    print(message)
print("total score is: ", score, "/", len(data))


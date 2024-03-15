Greeting = "Hello You"
file = open("../files/len_char.txt", 'w')
file.writelines(Greeting)

with open("../files/len_char.txt", 'r') as file:
    # print(file.read()) not so
    # print(len(file.read())) not so
    content = file.read()
    print(content)
    print(len(content))
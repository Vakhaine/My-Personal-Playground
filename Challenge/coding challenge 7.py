user_name = input("Enter a new member: ") + '\n'

file = open(r'../files/members.txt', 'r')
members = file.readlines()
file.close()
members.append(user_name)
file = open(r'../files/members.txt', 'w')
file.writelines(members)
file.close()



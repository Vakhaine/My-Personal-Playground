ips = ['100.122.133.105', '100.122.133.111']
user_input = int(input("Enter the index of the IP you want: "))

if user_input == 0 or user_input == 1:
    print('You chose', ips[user_input])
else:
    print("Invalid index. Please enter 0 or 1")
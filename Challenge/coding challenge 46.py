import csv

try:
    with open('../Challenge/weather.csv', 'r') as file:
        data = list(csv.reader(file))
        city = input("Enter a city: ")
    for row in data[0:]:
        if row[0] == city:
            temp = row[1]
            print(temp)
except FileNotFoundError:
    print("File not found. Check the file path and name.")
except Exception as e:
    print("An error occurred:", e)
filenames = ['d.txt', 'r.txt', 'p.txt']

for filename in filenames:
    file = open(f"../files/{filename}", 'w')
    file.write("Hello")
    file.close()
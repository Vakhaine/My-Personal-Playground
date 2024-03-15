filenames = ['../files/a.txt', '../files/b.txt', '../files/c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)

#file_2 = open(r'../files/b.txt')
#file_3 = open(r'../files/c.txt')

#for a, b, c in zip(file_1, file_2, file_3):
#    print(a)
#    print(b)
#    print(c)



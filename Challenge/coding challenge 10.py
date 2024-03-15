filenames = ['1.doc', '2.Report', '3.Presentation']

filename = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filename)

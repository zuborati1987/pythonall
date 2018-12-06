filename = "file.py"

infile = open(filename, 'r')
data = infile.read()
infile.close()

print(data)
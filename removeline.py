file1 = open('Codingal.txt', 'r')

file2 = open('CodingalUpdated.txt', 'w')

print(file1.read(8))
print(file1.readline())
for line in file1.readlines():
    if not(line.startswith('Shreyansh')):
        print(line)
        file2.write(line)

file1.close()
file2.close()
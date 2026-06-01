


outputFile = open('UpdatedFile.txt', "w")


inputFile = open('Repeated.txt', "r")


lines_seen_so_far = set()
print("Eliminating duplicate lines....")

for line in inputFile:


    if line not in lines_seen_so_far:


        outputFile.write(line)


        lines_seen_so_far.add(line)


inputFile.close()
outputFile.close()


inputFile = open('Repeated.txt', "r")


for line in inputFile:

    word = line.split()
    print(word)


inputFile.close()


import os


if os.path.exists("Normal.txt"):

    os.remove("Normal.txt")


else:

    print("The file does not exist")


os.rmdir("Removefolder")
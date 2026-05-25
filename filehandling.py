
fileread = open('Codingal.txt', 'r')
print("The file is in read mode")
print(fileread.read())
fileread.close()

file_write = open('Codingal.txt', 'w')

file_write.write("File in write mode ....")
file_write.write("Hi! I am Shreyansh. I am 10 years old.")
file_write.close()



fileread = open('Codingal.txt', 'r')
print("The file is in read mode")
print(fileread.read())
fileread.close()

file_write = open('Codingal.txt', 'a')

file_write.write("File is in a mode I do not know ....")
file_write.write("Hi! I am very real. I drink water.")
file_write.close()

fileread = open('Codingal.txt', 'r')
cnt = 0
content = fileread.read()
colist = content.split("\n")
for i in colist:
    if i:
        cnt+=1
print("The file is in read mode The number of lines", cnt)

fileread.close()
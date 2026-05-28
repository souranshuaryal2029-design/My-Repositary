fileread = open('Codingal.txt', 'r')
print("The file is in read mode")
print(fileread.read())
fileread.close()

file_write = open('Codingal.txt', 'w')

file_write.write("File in write mode ....")
file_write.write("Hi! I am Shreyansh. I am 10 years old.")
file_write.close()
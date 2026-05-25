fileread = open('Codingal.txt', 'r')
cnt = 0
content = fileread.read()
colist = content.split("\n")
for i in colist:
    if i:
        cnt+=1
print("The file is in read mode The number of lines", cnt)

fileread.close()
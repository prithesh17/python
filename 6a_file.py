import os
import sys
file_name = input("Enter the filename : ")
if not os.path.isfile(file_name):
    print("File", file_name, "doesn't exists")
    sys.exit(0)
infile = open(file_name, "r")
lineList = infile.readlines()
for i in range(10):
    print(i + 1, ":", lineList[i])
word = input("Enter a word : ")
cnt = 0
for line in lineList:
    cnt += line.count(word)
print("The word", word, "appears", cnt, "times in the file")


import os
#ask user for txt file name 

fopen= open('sampleInput.txt')

line_X = fopen.readline()


depth = 0

while line_X:

    mainLine = line_X.rstrip()
    line_X = line_X.strip()

    if(line_X == "{"):
        depth+=1

    print(str(depth) + mainLine)

    if(line_X == "}"):
        depth -= 1
    line_X = fopen.readline()

fopen.close()
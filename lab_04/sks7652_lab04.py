#ask user for txt file name 
fileName = input("Enter the file name : ")
print('\n')

#file is opened as read only in fopen 
fopen= open(fileName,'r')

#read the line from the opened file 
line_X = fopen.readline()

#nesting depth
depth = 0

while line_X:

    #remove the trailing character from the string, In this case space is the trailing character
    primaryLine = line_X.rstrip()
    
    line_X = line_X.strip()

    #every open curly braces except inside quote means 1 nesting depth
    if(line_X == "{"):
        depth += 1

    print(str(depth) + ' ' + primaryLine)

    #every closing curly braces except inside the quotes means -1 nesting depth
    if(line_X == "}"):
        depth -= 1

    #if there is no more lines to read the loop ends    
    line_X = fopen.readline()
#closing the opened file.
fopen.close()
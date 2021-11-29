filename = input("Enter you name : ")

fileOpen = open(filename,'r')


line = fileOpen.readline()

print(line)
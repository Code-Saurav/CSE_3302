#ask user for txt file name 
fileName = input("Enter the file name : ")
print('\n')

with open(fileName) as fopen:
   line = fopen.readline()
   count = 0
   while line:
        # if line.strip() == "{":
        #     count += 1
        # elif line.strip() == "}":
        #     count -= 1

        for character in line:
            if character == "/":
                pass
                if character =="/":
                    break
            else:

                if character == "{":
                    count += 1 
                if character == "}":
                    count -= 1

                    #todo : Ignore the braces inside the quotes
                    #todo : check the unmatched braces ( expected '}') but not found EOF ourput an error message
                    #todo : allow for multiple braces on the same lin e, fo rexmple """"
                    #tod : Handle block coments that cross multiple lines of the input file 
                    # /* comment with ignored braces { */


            # if character == "{":
            #     count += 1
            # if character == "}":
            #     count -= 1

        print("{} {}".format(count,line.strip()))       
            
                
        # print("{} {}".format(count, line.strip()))
        # if line.strip() == "}":
        #     count -= 1
        line = fopen.readline()

fopen.close()
# RohanRenganathan

# This is a compiler for Wilson's Langauge

import colorama
from colorama import Fore, Style


def errorMessage(currentLine, errorLineNum) :
    print(Fore.RED + "The error is on line number " + str(errorLineNum))
    print('"' + currentLine + '"')


keyWords = ["DEF", "INT", "STR", "BOOL", "IF", "THEN", "ENDIF", "LOOP", "ENDLOOP", "PRINT", "START", "END"]
dataTypes = ["INT", "STR", "BOOL"]


#fileName = input ("What is the name of the file? ")

fileName = "WilsonsLanguage.wl"
inputFile = open(fileName, "r")
lineNum = 0
codeLineNum = 0
varName = ""



# checs the lines contained in the file
while line := inputFile.readline():
    lineNum = lineNum + 1
    line = line.strip()

    # checs whether the line is blan or a comment
    if not line or line.startswith("*"):
        continue

    codeLineNum += 1

    # first line must be "START"
    if codeLineNum == 1 and not line.startswith("START "):
        errorMessage(line, lineNum)
        print("The first line of the program must begin with START")
        exit()

    # continues to 2nd line if first line is START
    elif codeLineNum == 1 and line.startswith("START ") :
        continue

    # every line must end with ; except the START line
    if line[-1] != ";" and not line.startswith("START "):
        errorMessage(line, lineNum)
        print("Every line must end with a ; \n")
        exit()

    # splits the words present on the line into a list
    lineWords = line.split()

    # checks that all keywords are in upper case
    for i in range(0, len(lineWords)):
        if (lineWords[i].islower()) and (lineWords[i].upper() in keyWords) :
            errorMessage(line, lineNum)
            print ("The keyword " + lineWords[i] + " should be in upper case \n")
#           print ("The keywords are: DEF, INT, STR, BOOL, IF, THEN, ENDIF, LOOP, ENDLOOP, PRINT, START, END")
            exit()


#           raise Exception ("The eyword " + lineWords[i] + " should be in upper case" + "File " + '"'+fileName+'"' + " , line " + str(lineNum))

    if lineWords[0] == "DEF" :

        if lineWords[-1][:-1] not in dataTypes :
            errorMessage(line, lineNum)
            print("This is not a valid data type \n")
            exit()

        # checks that a variable does not contain spaces
        elif lineWords.index("as") > 2 :
            errorMessage(line, lineNum)
            print ("The variable must not contain spaces \n")
            exit()

        # checks that the first letter of a variable is a letter
        elif not lineWords[1][:1].isalpha() :
            errorMessage(line, lineNum)
            print ("Variable names must start with a letter \n")
            exit()

        # checks that IF statements end with THEN on the same line
        if lineWords[0] == "IF" and lineWords[-1] != "THEN" :
            errorMessage(line, lineNum)
            print("IF statements must end with THEN and they must be on the same line \n")
            exit()



with open (fileName, "r") as f :
    data = f.read()
    lines = data.splitlines()
    lastLine = lines[-1]

    # counts the number of LOOP and ENDLOOP present
    totalLoop = (data.count("LOOP") - data.count("ENDLOOP"))
    totalEndLoop = (data.count("ENDLOOP"))


    totalIF = (data.count("IF") - data.count("ENDIF"))
    totalENDIF = (data.count("ENDIF"))

    if totalIF != totalENDIF :
        errorMessage(line, lineNum)
        print ("Every '"'IF'"' statement should end with '"'ENDIF'"' \n")
        exit()

    # checks that every LOOP statement has an ENDLOOP
    if totalLoop != totalEndLoop :
        errorMessage(line, lineNum)
        print("Every '"'LOOP'"' statement should end with '"'ENDLOOP'"' \n")
        exit()

# checks that the last line of the program is END
if lastLine[0:3] != "END" :
    print ("The last line is " + lastLine)
    print(Fore.RED + "File " + '"' + fileName + '"' + " , line " + str(lineNum))
    print (Fore.RED + "The last line of the program must be '"'END'"' \n")
    exit()


inputFile.close()

print (Fore.GREEN + fileName + " compiled successfully!")

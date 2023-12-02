import os

letterDigit = {
        "one" : '1',
        "two" : '2',
        "three" : '3',
        "four" : '4',
        "five" : '5',
        "six" : '6',
        "seven" : '7',
        "eight" : '8',
        "nine" : '9',
}
letterDigitKeys = [d for d in letterDigit]

#This function needs to replace the first and last instance of a digit in letter form found
#Frustratingly, I could not think of a better solution in one sitting
def letterToDigit(cLine):
    check = [d for d in letterDigitKeys if d in cLine]
    if not check:
        return cLine
    ccLine = cLine
    sub = ""
    #Starting from front of string -> end of string
    for i in range(len(cLine) - 2):
        sub = ccLine[0:(3+i)]
        if any(d for d in letterDigitKeys if d in sub):
            for k in check:
                sub = sub.replace(k, letterDigit[k])
            ccLine = sub + ccLine[3+i:]
            break
    sub = ""
    #Starting from end of string -> front of string
    for i in reversed(range(len(cLine) - 2)):
        sub = ccLine[i:]
        if any(d for d in letterDigitKeys if d in sub):
            for k in check:
                sub = sub.replace(k, letterDigit[k])
            ccLine = ccLine[:i] + sub
            break
    return ccLine
        
        
#Get current directory and find file full of inputs
current_directory = os.getcwd()
target = "puzzle_input.txt"
target_fpath = os.path.join(current_directory, target)

#Created a list of every line called calibrationList - pt1
with open(target_fpath, 'r') as file:
        calibrationList = [line.rstrip('\n') for line in file.readlines()]

#List for all calibration numbers per line - pt1
numList = []
test = []
#Get calibration number per line in calibrationList - pt1
for cl in calibrationList:
        dLine = letterToDigit(cl)
        print(dLine)
        #Filter string to just numbers by checking if it's numeric - pt1
        numberLine = "".join(c for c in dLine if c.isnumeric())

        fChar = numberLine[0]
        lChar = numberLine[-1]
        caliNum = fChar+lChar
        
        numList.append(int(caliNum))
#Result
print(sum(numList))


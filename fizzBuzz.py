def create1to101Array(theArray):
    for loopCounter in range(1, 101):
        theArray.append(loopCounter)
    return theArray


def printFizzBuzz(theArray):
    for loopCounter in theArray:
        if(loopCounter%3==0 and loopCounter%5==0):
            print("Number: ", loopCounter, ". FIZZBUZZ")
        elif(loopCounter % 3 == 0):
            print("Number: ", loopCounter, ". FIZZ")
        elif(loopCounter % 5 == 0):
            print("Number: ", loopCounter, ". BUZZ")
        else:
            print("It's just: ", loopCounter)


arrayForTheExercise = []
newArrayForTheExercise = create1to101Array(arrayForTheExercise)
printFizzBuzz(newArrayForTheExercise)
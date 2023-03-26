#Karena Qian
#Professor Carlos Arias
#Iterative vs Recursive
#Last modified: January 16, 2023
#This program calculates the time it take for an iterative
#and a recursive function to execute for a range of values
import timeit #timeit measures wall time (also known as clock time or wall-clock time) of the total time elasped from the start to the end of a program's execution

#definition of iter function for setup (won't factor in execution time)
#iterativePower - returns the base raised to the exponent using iteration
#Params: base (the base of the power) exponent (the exponent of the power)
#Returns: the base raised to the exponent

setupIter = '''def iterativePower(base, exponent):
    result = 1.0
    if (exponent < 0):
        return 1.0 / iterativePower(base, -exponent)
    else:
        for x in range(exponent):
            result *= base
    return result'''

#definition of recurse for setup (won't factor in execution time)
#recursivePower - returns the base raised to the exponent using recursion
#Params: base (the base of the power) exponent (the exponent of the power)
#Returns: the base raised to the exponent

setupRecurs = '''def recursivePower(base, exponent):
    if(exponent < 0):
        return 1.0 / recursivePower(base, -exponent)
    elif(exponent == 0):
        return 1.0
    else:
        return base * recursivePower(base, exponent - 1)'''

#largest possible max (from 0): 983 (otherwise stackoverflow risk (Python gives recursion error))
#time unit: nanoseconds (ns)

f = open("comp.csv", "w") #creates/opens the comp.csv file for writing in
#executes both iterativePower and recursivePower functions from 0 to 983 (largest possible max)
for x in range(984):
    #calling statement (the actual execution of iter fn)
    iterStmt = "iterativePower(3.14159265359, {})" 
    #calling statement (the actual execution of recurse fn)
    recursStmt = "recursivePower(3.14159265359, {})" 
    csvLine = "{0},{1},{2}\n" #format for a single line in the CSV file
    f.write(csvLine.format(x, 
        (timeit.timeit(setup=setupIter, stmt=iterStmt.format(x), 
            number=100)/100) * 10**9, 
        (timeit.timeit(setup=setupRecurs, stmt=recursStmt.format(x), 
            number=100)/100) * 10**9))
f.close() #closes the CSV file




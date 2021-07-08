# Problem Name is  Pascals Triangle  PLEASE DO NOT REMOVE THIS LINE.

"""
/*
** The below pattern of numbers are called Pascals Triangle. 
**
** Pascals Triangle exhibits the following behaviour: 
**
** The first and last numbers of each row in the triangle are 1 
** Each number in the triangle is the sum of the two numbers above it. 
**
** Example: 

**  	1 
**     1 1 
**    1 2 1
**   1 3 3 1
    1 4 6 4 1
  1 5 10 10 5 1
1 6 15 20 15 6 1
**
** Please Complete the 'pascal' function below so that given a 
** col and a row it will return the value in that positon. 
**
** Example, pascal(1,2) should return 2 
**
*/
"""
def pascal(col, row):
	if col==0 or row==0 or row==col:
	    return 1
	else:
	    return pascal(col-1,row-1)+pascal(col,row-1)
        
def doTestPass():
	""" Returns 1 if all tests pass. Otherwise returns 0. """
	doPass = True 
	pascalColRowValues={(0,0):1,(1,2):2,(5,6):6,(5,5):1}
	for key, val in pascalColRowValues.items(): 
	    if pascal(key[0],key[1]) != val:
	        doPass = False 
	        print("Failed for {} and {} \n", format(key, val))
	if doPass: 
	    print("All tests pass\n") 
	    return doPass 

if __name__ == "__main__":
    doTestPass() 
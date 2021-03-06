# Problem Name is &&& SubArray Exceeding Sum &&& PLEASE DO NOT REMOVE THIS LINE. 
'''
    Instructions to candidate.
    1) Your task is ultimately to implement a function that takes in an array of non-negative numbers and an integer.
    You want to return the *LENGTH* of the shortest subarray whose sum is at least the integer, and -1 if no such sum exists.
    2) Run this code in the REPL to observe its behaviour. The execution entry point is main().
    3) Consider adding some additional tests in doTestsPass().
    4) Implement subArrayExceedsSum() correctly.
    5) If time permits, some possible follow-ups. 
'''

def subArrayExceedsSum(arr, target):
    # todo: implement here 
    if(sum(arr)<target):
        return -1
    m=len(arr)+1
    for i in range(0,len(arr)):
        curr=arr[i]
        if(curr>=target):
            return 1
        for j in range(i+1,len(arr)):
            curr+=arr[j]
            if curr>=target and j-i+1<m:
                m=j-i+1
    return m
    

def doTestsPass():
    """ Returns 1 if all tests pass. Otherwise returns 0. """
    testArrays = [[[1,2,3,4], 6], [[1,2,3,4], 12],[[0,0,0,0],0]]
    testAnswers = [2, -1,1] 
    for i in range( len( testArrays ) ):
        if not ( subArrayExceedsSum( testArrays[i][0], testArrays[i][1] ) == testAnswers[i] ):
            return False 
    return True 

if __name__ == "__main__":
    if( doTestsPass() ):
        print( "All tests pass" )
    else:
        print( "Not all tests pass" ) 

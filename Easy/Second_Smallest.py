# Problem Name is &&& Second Smallest &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate.
1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
2) Consider adding some additional tests in doTestsPass().
3) Implement secondSmallest() correctly.
4) If time permits, some possible follow-ups.
"""

def secondSmallest(x):
    """ Returns second smallest element in the array x. Returns nothing if array has less than 2 elements. """
    # todo: implement here return
    if len(x)<2:
        return
    else:
        minf,mins=x[0],x[1]
        if x[0]>x[1]:
            mins=x[0]
            minf=x[1]
        
        for i in range(2,len(x)):
            if(x[i]<minf):
                mins=minf
                minf=x[i]
            elif x[i]<mins:
                mins=x[i]
        return mins

def doTestsPass():
    """ Returns 1 if all tests pass. Otherwise returns 0. """
    testArrays = [ [0], [0,1] ,[1,1,7,6,3,5,8]]
    testAnswers = [ None, 1,1]
    for i in range( len( testArrays ) ):
        if not ( secondSmallest( testArrays[i] ) == testAnswers[i] ):
            return False
    return True

if __name__ == "__main__":
    if( doTestsPass() ):
        print( "All tests pass" )
    else:
        print( "Not all tests pass" ) 
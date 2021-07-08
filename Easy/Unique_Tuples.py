# Problem Name is &&& Unique Tuples &&& PLEASE DO NOT REMOVE THIS LINE. 
""" 
Instructions to candidate.
1) Run this code in the REPL to observe its behaviour. The execution entry point is main.
2) Consider adding some additional tests in doTestsPass().
3) Implement uniqueTuples() correctly.
4) If time permits, some possible follow-ups. 
"""
"""
Given a string and size of the tuples, extracts all unique tuples(substrings) of the given size.
"""
import itertools
def uniqueTuples( input, size ):
    """ TODO: Implement solution"""
    m=itertools.permutations(input,size)
    result=set(m)
    return result

""" Returns 1 if all tests pass. Otherwise returns 0. """
def doTestsPass():
    """# TODO: implement some tests, please # we've included a trivial boilerplate """
    testPassed = True
    result = set()
    testString = "aab"
    goodResult = set()
    goodResult.add( "aa" )
    goodResult.add( "ab" )
    result = uniqueTuples( testString, 2 )
    if( result.symmetric_difference_update( goodResult ) == None ):
        print( "Test passed." )
        testPassed = True
    else:
        print( "Test failed." )
        testPassed = False
    return testPassed

if __name__ == "__main__":
    doTestsPass()
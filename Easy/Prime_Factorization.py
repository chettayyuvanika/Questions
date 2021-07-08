#Instructions to candidate.
"""
1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
2) Consider adding some additional tests in doTestsPass().
3) Implement primeFactorization() correctly.
4) If time permits, some possible follow-ups. 
"""

"""
Return an array containing prime numbers whose product is x
    Examples: 
        primeFactorization(6) == [2,3]
        primeFactorization(5) == [5]
        primeFactorization(12) == [2,2,3]
"""
import math
def primeFactorization(x):
    # todo: implement here
    l=[]
    if x<2:
        return
    n=x
    for i in range(2,math.ceil(n**0.5)+1):
        while x%i==0:
            l.append(i)
            x=x/i
    return l

def doTestsPass():
    """ Returns True if all tests pass. Otherwise returns False. """
    testVals = [6,8,6859,1062347,1]
    testAnswers = ([2, 3],[2,2,2],[19,19,19],[11,13,17,19,23],None)

    for value, answer in zip(testVals, testAnswers):
        
        if primeFactorization(value) != answer:
            print ("Test failed for %d" % value)
            return False
    return True

if __name__ == "__main__":
    if doTestsPass():
        print ("All tests pass")
    else:
        print ("Not all tests pass")

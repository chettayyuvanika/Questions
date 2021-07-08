# 4 Problem Name is &&& Is Power of 10 &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate.
1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
2) Consider adding some additional tests in doTestsPass().
3) Implement isPower0110() correctly.
4) If time permits, some possible follow-ups.
"""
def isPowerOfl0(x):
    """ Returns 1 if x is a power-of-10. Otherwise returns 0. """
    #todo: implement here return False
    if x==1:
        return 1
    elif x<9:
        return 0
    else:
        return isPowerOfl0(x//10)

def doTestsPass():
    """ Returns 1 if all tests pass. Otherwise returns 0. """
    #todo: implement more tests, please
    #feel free to make testing more elegant
    doPass = True
    powersOf10 = [10,1000,100000]
    notPowersOf10 = [5,50]

    for n in powersOf10:
        if not isPowerOfl0(n):
            print("Failed for " + str(n) + "\n")
            doPass = False

    for n in notPowersOf10:
        if isPowerOfl0(n):
            print("Failed for " + str(n) + "\n")
            doPass = False

    if doPass:
        print("All tests pass\n")

    return doPass

if __name__ == "__main__":
    doTestsPass()
"""
Instructions to candidate. 
    1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
    2) Consider adding some additional tests in doTestsPass().
    3) Implement findFirst(str) correctly.
    4) If time permits, some possible follow-ups. 
"""

"""
Finds the first character that does not repeat anywhere in the input string 
If all characters are repeated, return 0 
Given "apple", the answer is "a" 
Given "racecars", the answer is "e" 
Given "ababdc", the answer is "d" 
"""
from collections import Counter
def findFirst(str): 
    #todo: implement solution
    a=Counter(str)
    for i in str:
        if(a[i]==1):
            return i
    
"""
Returns true if all tests pass. Otherwise returns false.
"""
def doTestsPass():
    
    
    #todo: implement more tests
    doPass = True
    tests = {"racecar":'e', "apple":'a', "ababdc":'d',"aaaa":None,"aaaaaac":'c' } 
    for test in tests.items(): 
        result = findFirst(test[0]) 
        if result != test[1]: 
            print("Test Failed: " + test[0] + " expected:" + test[1] + " actual: " + result + "\n")
            return False 
    return True 


if __name__ == "__main__":
    result = doTestsPass()
    
    if result:
        print("All tests pass\n");
    else:
        print("Tests fail\n");












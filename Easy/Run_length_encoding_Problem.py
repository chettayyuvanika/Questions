# Problem Name is Run Length Encoding  PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate.
1) Run this code in the REPL to observe its behaviour. 
2) Consider adding some additional tests in doTestsPass(). 
3) Implement rle() correctly. 
4) If time permits, try to improve your implementation. 
Implement a run length encoding function. 

For a string input the function returns output encoded as follows: 
    
"a" -> "al" 
"aa" -> "a2" 
"aabbb" -> "a2b3" 
"aabbbaa" -> "a2b3a2" 
"""

def rle(testString):
	"""
	  TODO: ad solution here
	"""
	result = ""
	k=[]
	t=testString[0]
	s=testString[0]
	if(len(testString)==1):
	    k.append(testString)
	else:
	    for i in range(1,len(testString)):
	        if testString[i]==t:
	            s+=testString[i]
	        else:
	            k.append(s)
	            t=testString[i]
	            s=testString[i]
	    k.append(s)
	for i in k:
	    result+=i[0]+str(len(i))
	return result

def Assert(actual,expected, message):
    if(actual == expected):
        print("PASSED: ", message, "Actual %s == Expected %s" % (actual, expected)); 

    else: 
        print("FAILED: ", message, "Actual %s != Expected %s" % (actual, expected)); 

def doTestsPass(): 
    Assert(rle("aaa"),   "a3",    "Example 1"  );
    Assert(rle("aabbc"),  "a2b2c1",  "Example 5"  );
    Assert(rle("abbbccdde"),  "a1b3c2d2e1",  "Example 6"  );
    Assert(rle("a"),  "a1",  "Example 7"  );

if __name__ == "__main__":
    doTestsPass() 

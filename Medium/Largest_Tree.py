"""
** Instructions:
** Given a forest ( one or more disconnected trees ), find the root of largest tree
** and return its Id. If there are multiple such roots, return the smallest Id of them. 
**
** Complete the largestTree function in the editor below.
** It has one parameter, immediateParent, which is a map containing key-value pair indicating
** child -> parent relationship. The key is child and value is the corresponding
** immediate parent.
** Constraints
**      - Child cannot have more than one immediate parent.
**      - Parent can have more than one immediate child.
**      - The given key-value pair forms a well-formed forest ( a tree of n nodes will have n-1 edges )
** Example:
** 
** Input: 
** { { 1 -> 2 }, {3 -> 4} } 
** 
** Expected output: 2
** Explanation: There are two trees one having root of Id 2 and another having root of Id 4.
** Both trees have size 2. The smaller number of 2 and 4 is 2. Hence the answer is 2.
"""

"""Find the largest tree. """ 
def largestTree(immediateParent):
    #TODO: implement this function
    d=dict()
    for i in immediateParent:
        if(immediateParent[i] in d):
            d[immediateParent[i]].append(i)
        else:
            d[immediateParent[i]]=[i]
    m=0
    out=sorted(d)[-1]
    for i in d:
        if(len(d[i])>m):
            m=len(d[i])
            out=i
        elif len(d[i])==m:
            if(i<out):
                out=i
    return out 
def doTestsPass():
    """ Returns true if the tests pass. Otherwise, returns false """ 
    testCases = [
        (dict({1:2, 3:4}), 2),
        (dict({1:2, 3:4 , 5:4}), 4)
    ] 
    
    passed = True
    for tc, expected in testCases:
        actual = largestTree(tc)
        if actual != expected:
            passed = False
            print("Failed for case ", tc, "\n expected ", expected, ", actual ", actual) 
    return passed 
if __name__ == "__main__": 
    result = doTestsPass() 
    if result:
        print("All tests pass\n")
    else:
        print("Tests fail\n");

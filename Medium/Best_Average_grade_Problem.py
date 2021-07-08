# Problem Name is &&& Best Average Grade &&& PLEASE DO NOT REMOVE THIS LINE. 

"""
Instructions: 
Given a list of student test scores, find the best average grade. Each student may have more than one test score in the list. 
Complete the bestAverageGrade function in the editor below. It has one parameter, scores, which is an array of student test scores. Each element in the array is a two-element array of the form [student name, test score] e.g. [ "Bobby", "87" ]. Test scores may be positive or negative integers. 
If you end up with an average grade that is not an integer, you should use a floor function to return the largest integer less than or equal to the average. Return 0 for an empty input. 

Example:
Input:
[ [ "Bobby", "87" ],
[ "Charles", "100" ], 
[ "Eric", "64" ], 
[ "Charles", "22" ] ].

Expected output: 87

Explanation: The average scores are 87, 61, and 64 for Bobby, Charles, and Eric, respectively. 87 is the highest. 
"""

""" Find the best average grade. """ 
def bestAverageGrade(scores): 
	""" Returns true if the tests pass. Otherwise, returns false """
	# TODO: implement more test cases
	d=dict()
	for i in scores:
	    if i[0] in d:
	        d[i[0]].append(int(i[1]))
	    else:
	        d[i[0]]=[int(i[1])]
	avg=0
	for i in d:
	    avg1=sum(d[i])//len(d[i])
	    if avg1>avg:
	        avg=avg1
	return avg
	    
	
	

def doTestsPass():
    """ Returns true if the tests pass. Otherwise, returns false """ 

	# TODO: implement more test cases
    tc1 = [ [ "Bobby", "87" ], [ "Charles", "100" ], [ "Eric", "64" ], [ "Charles", "22" ] ];
    return bestAverageGrade(tc1)==87
    
if __name__ == "__main__":
    result = doTestsPass() 
    if result: 
        print("All tests pass\n"); 

    else:
	    print("Tests fail\n");


	
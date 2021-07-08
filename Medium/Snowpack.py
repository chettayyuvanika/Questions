# Problem Name is &&& Snowpack &&& PLEASE DO NOT REMOVE THIS LINE. 
'''
 Instructions to candidate.
    1) Given an array of non-negative integers representing the elevations 
        from the vertical cross section of a range of hills, determine how
        many units of snow could be captured between the hills. 
        
        See the example array and elevation map below. 
        
                                                                 ___
                        ___                |   |        ____
                       |   |        ___    |   |___    |    |
                ___|   |    ___|   |   |   |   |   |   |
        ___|___|___|___|___|___|___|___|___|___|___|___
        [0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0]
        
                                                                 ___
                        ___                |   |        ____
                       |   | *   *  _*_  * |   |_*_  * |    |
                ___|   | *  _*_|   | * |   |   | * |   |
        ___|___|___|_*_|___|___|_*_|___|___|_*_|___|___
        [0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0]
        
        Solution: In this example 13 units of snow (*) could be captured. 
    2) Consider adding some additional tests in doTestsPass(). 
    3) Implement computeSnowpack() correctly. 
'''
def computeSnowpack(arr):
    # Todo: Implement computeSnowpack
    sum = 0
    l=0
    r=0
    low=0
    high=len(arr)-1
    while(low<=high):
        if(arr[low]<arr[high]):
            if(arr[low]>l):
                l=arr[low]
            else:
                sum+=l-arr[low]
            low+= 1
        else:
            if(arr[high]>r):
                r=arr[high]
            else:
                sum+=r-arr[high]
            high-= 1
    return sum

def doTestsPass(): 
    """ Returns True if all tests pass. Otherwise returns False. """
    tests = [[[0,1,3,0,1,2,0,4,2,0,3,0], 13],[[1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],6]] 
    for test in tests:
        if not (computeSnowpack(test[0]) == test[1]):
            return False 
    return True 

if __name__ =="__main__":
    if(doTestsPass()):
        print("All tests pass")
    else:
        print("Not all tests pass")






'''Instructions to candidate.
1) You are an avid rock collector who lives in southern California. Some rare 
        and desirable rocks just became available in New York, so you are planning
        a cross-country road trip. There are several other rare rocks that you could
        pick up along the way. 
        
        You have been given a grid filled with numbers, representing the number of
        rare rocks available in various cities across the country. Your objective
        is to find the optimal path from So_Cal to New_York that would allow you to
        accumulate the most rocks along the way. 
        
        Note: You can only travel either north (up) or east (right).
        
2) Consider adding some additional tests in doTestsPass().
3) Implement optimalPath() correctly.
4) Here is an example: 
            [[0,0,0,0,5], New_York (finish)     N
             [0,1,1,1,0],                   < W E >
    So_Cal (start) [2,0,0,0,0]] 
    
    The total for this example would be 10 (2+0+1+1+1+0+5). '''
 
  
def optimal_path(grid):
    # Todo: Implement optimalPath return 0
    a=[[0 for i in range(len(grid[0]))]for j in range(len(grid))]
    a[len(grid)-1][0]=grid[len(grid)-1][0]
    for i in range(1,len(grid)):
        a[len(grid)-1][i]=a[len(grid)-1][i-1]+grid[len(grid)-1][i]
    for i in range(len(grid)-2,-1,-1):
        a[i][0]=a[i+1][0]+grid[i][0]
    for i in range(len(grid)-2,-1,-1):
        for j in range(1,len(grid[0])):
            a[i][j]=max(a[i+1][j],a[i][j-1])+grid[i][j]
    return a[0][len(grid[0])-1]


def do_tests_pass():
    """ Returns True if all tests pass. Otherwise returns False. """
    test_inputs = [[[0, 0, 0, 0, 5],
                    [0, 1, 1, 1, 0],
                    [2, 0, 0, 0, 0]]] 
    test_answers = [10] 
    
    for test_input, test_answer in zip(test_inputs, test_answers):
        if optimal_path(test_input) != test_answer:
            return False 
    return True 
    
if __name__ =="__main__":
    if do_tests_pass():
        print('All tests pass')
    else:
        print('Not all tests pass')
        

 
 

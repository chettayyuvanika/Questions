# Problem Name is &&& Staircase &&& PLEASE DO NOT REMOVE THIS LINE. 
''' 
    Instructions: 
    There is a staircase with 'n' number of steps. A child
    walks by and wants to climb up the stairs, starting at
    the bottom step and ascending to the top.
    
    Of course, the child wants to have fun, too, so instead
    of taking 1 step at a time, she will vary between taking
    either 1, 2 or 3 steps at a time.
    
    Please complete the 'countSteps' method below so that
    given 'n' number of steps it will return the number of
    unique combinations the child could traverse. 
    
    An example would be countSteps(3) == 4: 
    
    1 1 1
    2 1
    1 2
    3
'''

''' Given n steps, returns the number of possible permutations
        to climb the staircase.
    Returns 0 when the input n is <= 0.'''

def countSteps(n):
    a=[]
    a.append(1)
    a.append(1)
    a.append(2)
    for i in range(3,n+1):
        a.append(a[i-1]+a[i-2]+a[i-3])
    return a[n]
        
def doTestsPass():
    """ Returns 1 if the tests pass. Otherwise, returns 0; """ 
    # todo: implement more tests, if you'd like 
    return (countSteps(3) == 4 and countSteps(4) == 7) 
    
if __name__ == "__main__":
    result = doTestsPass() 
    
    if result:
        print("All tests pass\n")
    else:
        print("Tests fail\n")
    for i in range(5):
        print("%d steps => %d\n" % (i+1, countSteps(i+1)))
        
        
        
        
        
        
        

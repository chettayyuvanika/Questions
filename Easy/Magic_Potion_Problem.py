# Problem Name is Magic Potion PLEASE DO NOT REMOVE THIS LINE. 

"""
Instructions to candidate. 
1) Run this code in the REPL to observe its behaviour. The execution entry point is main. 
2) Consider adding some additional tests in do_tests_pass().
3) Implement minimal_steps() correctly. 
4) If time permits, some possible follow-ups. 


Question: Hermione is preparing a cheat-sheet for her final exam in Potions class. To create a potion, one must combine ingredients in a specific order, any of which may be repeated.


As an example, consider the following potion which uses 4 distinct ingredients (A,B,C,D) in 11 steps: A, 6, A, 6, C, A, 6, A, 6, C, D 
Hermione realizes she can save tremendous space on her cheat-sheet by introducing a special instruction, '*', which means "repeat from the beginning". 


Using these optimizations, Hermione is able to encode the potion above using only 6 characters: A,B,*,C,*,D 

Your job is to write a function that takes as input an un-encoded potion and returns the minimum number of characters required to encode the potion on Hermione's Cheat Sheet. 

"""

# Function to return the minimal number of steps 
def minimal_steps( ingredients ): 
    count=1
    i=1
    while(i<len(ingredients)):
        if(ingredients[i]==ingredients[0]):
            if(ingredients[0:i]==ingredients[i:i+i]):
                count+=1
                i=i+i-1
            else:
                count+=1
        else:
            count+=1
        i+=1
    return count
"""
Returns true if all tests pass. Otherwise returns false. 
TODO: implement some tests. We've included a trivial boilerplate 
"""

def do_tests_pass(): 
	return (minimal_steps( "ABCDABCE" ) == 8 and minimal_steps( "ABCABCE" ) == 5 and minimal_steps("A6A6CA6A6CD")==6)

if __name__=="__main__":
    result = do_tests_pass() 
    if result: 
        print( "All tests passed" ) 
    else: 
        print( "Tests failed" ) 

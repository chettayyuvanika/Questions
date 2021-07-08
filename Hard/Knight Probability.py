# Problem Name is &&& Knight Probability &&& PLEASE DO NOT REMOVE THIS LINE.

"""

Instructions: 

Given an empty chessboard (8x8 grid), a knight is placed
on one of the squares. The knight 'K' at position (3, 3)
and it's possible movements 'X' are shown in the example 
below: 

        ********
        **X*X***
        *X***X**
        ***K****
        *X***X**
        **X*X***
        ********
        ********

Depending on the knight's position on the board, 0-6 of 
the 8 possible movements may cause the knight to leave 
the chess board. 

If the knight moves n times, each time choosing one of
the 8 possible moves uniformly at random, determine the 
probability that the knight is still on the board after
making n random moves. After the knight has left the 
board, it may not reenter. 

Please implement the method probability which given a 
start position x, y, and a number of moves n, 
returns the probability a knight remains on the board 
as described above. 

"""
def probability(x, y, n): 
    moves=[[2,-1],[2,1],[1,-2],[1,2],[-1,-2],[-1,2],[-2,-2],[-2,1]]
    prob=[[[1]*11]*8]*8
    for step in range(1,n+1):
        for i in range(8):
            for j in range(8):
                probs=0.0
                for k in range(8):
                    posx=i+moves[k][0]
                    posy=j+moves[k][1]
                    if posx>=0 and posx<8 and posy>=0 and posy<8:
                        probs+=prob[posx][posy][step-1]
                prob[i][j][step]=probs/8.0
    
    return prob[x][y][n]
    
    
def do_tests_pass(): 
    #Returns True if the tests pass. Otherwise, returns False 
    test_cases = {
        #Start in a corner, no moves 
        (0, 0, 0): 1.0, 
        #Start in the middle, one move 
        (3, 3, 1): 1.0, 
        #Start in a corner, one move 
        (0, 0, 1): 0.25, 
        
    }
    # todo: feel free to enhance or add more test cases 
    for case, expected in test_cases.items():
        if probability(case[0], case[1], case[2]) != expected: 
            return False
        return True 
        
if __name__ == "__main__": 
    
    if do_tests_pass(): 
        print("All tests pass")
    else: 
        print("Tests fail")


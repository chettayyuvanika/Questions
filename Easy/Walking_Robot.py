# Problem Name is &&& Walking Robot &&& PLEASE DO NOT REMOVE THIS LINE. 
# Instructions to candidate # 1. Run this code in the REPL to observe its behaviour. The • execution entry point is main().
# 2. Implement the 'walk' method. This method takes in a string, path, • where each character in the string corresponds to a potential movement • of the robot. The robot can move up, down, left, and right represented • by the characters 'U', 'D', 'L', and 'R' respectively. All other • characters may be ignored. Assume the robot's initial position • is at (0,0). The output of this method is the robot's final x and y • coordinates relative to the initial position.
# 3. Consider adding more test cases 
def walk( path ):
    # TODO: Implement solution return( [0,0] )
    x,y=0,0
    i=0
    while(i<len(path)):
        if path[i] in "ULDR":
            if path[i]=="U":
                y+=1
            elif path[i]=="L":
                x-=1
            elif path[i]=="D":
                y-=1
            else:
                x+=1
        elif path[i] in "0123456789":
            amt=int(path[i])
            dir=path[i+2]
            if dir=="U":
                y+=amt
            elif dir=="L":
                x-=amt
            elif dir=="D":
                y-=amt
            else:
                x+=amt
            i+=amt
        i+=1
    return( [x,y] )

def do_tests_pass():
    """ Returns True if all tests pass. Otherwise returns False. """
    """# TODO: implement some tests, please # we've included a trivial boilerplate """
    # path, expected
    test_cases = [ "UUU", [0, 3] ], [ "ULDR", [0, 0] ], [ "ULLLDUDUURLRLR", [-2,2] ], [ "UP LEFT 2xDOWN DOWN RIGHT RIGHT UP UP", [1,0],["",[0,0]] ]
    result = True
    for test in test_cases:
        result = result and ( walk( test[0] ) == test[1] )
    if result:
        print("Test passed.")
        return True
    else:
        print("Test failed.")
        return False

if __name__ == "__main__":
    do_tests_pass()
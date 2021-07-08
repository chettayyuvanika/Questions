#Problem Name is &&& ApacheLog &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate. 
1) Run this code in the REPL to observe its behaviour. The 
       execution entry point is specified at the bottom.
2) Consider adding some additional tests in do_tests_pass(). 
3) Implement find_top_ip_address() correctly.
4) If time permits, try to improve your implementation. 
"""
from collections import defaultdict
def find_top_ip_address(lines): 
    """ Given an Apache log file, return IP address(es) which accesses the site most often.

        Our log is in this format (Common Log Format). One entry per line and it starts with an IP address which accessed the site, followed by a whitespace.
        
        10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] "GET /a.gif HTTP/1.0" 200 234
        
        Log file entries are passed as a list. 
    """
        # todo: implement logic 
    lis=defaultdict(int)
    for i in lines:
        lis[i.split(" ")[0]]+=1
    m=0
    for i in lis:
        if lis[i]>m:
            m=lis[i]
            out=i
    return out
def do_tests_pass(): 
    lines = ["10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] \"GET /a.gif HTTP/1.0\" 200 234","10.0.0.1 - frank [10/Dec/2000:12:34:57 -0500] \"GET /b.gif HTTP/1.0\" 200 234", "10.0.0.2 - nancy [10/Dec/2000:12:34:58 -0500] \"GET /c.gif HTTP/1.0\" 200 234"] 
    result = find_top_ip_address(lines) 
    if result == "10.0.0.1":
        print("test passed") 
        return True 
    else: 
        print("test failed") 
    return False 
if __name__ == "__main__": 
    do_tests_pass() 


# Problem Name is &&& Deque &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions: 
1) Implement a double-ended queue (abbreviated to deque) that stores strings. 
    A deque is a data structure that has characteristics of both a queue and a stack. Elements can be added or removed from either the 
2) Consider adding some additional tests in doTestsPass() 

"""
import traceback 
class Deque: 
    def __init__(self):
        self.s=""
    def addFirst(self, data): 
        self.s=data+self.s
    def addLast(self, data):
        self.s+=data 
    def removeFirst(self):
        if(len(self.s)==0):
            return "Empty Deque"
        self.s=self.s[1:] 
    def removeLast(self): 
        if(len(self.s)==0):
            return "Empty Deque"
        self.s=self.s[:-1] 
    def peekFirst(self): 
        if(len(self.s)==0):
            return "Empty Deque"
        return self.s[0] 
    def peekLast(self): 
        if(len(self.s)==0):
            return "Empty Deque"
        return self.s[-1] 
    def getSize(self): 
        return len(self.s)
    def printd(self):
        print(self.s)

    
def assertTrue(condition, message): 
    if not condition: 
        raise Exception(message) 
def doTestsPass(): 
    deque=Deque() 
    deque.addLast("a")
    deque.addLast("b") 
    assertTrue(deque.getSize() == 2, "Test failed, getSize should be 2") 
    assertTrue("a" == deque.peekFirst(), "First element should be 'a'") 
    deque.addFirst("c")
    assertTrue("c" == deque.peekFirst(), "First element should be 'c'")
    assertTrue("b" == deque.peekLast(), "Last element should be 'b'")
    deque.removeFirst()
    assertTrue("a" == deque.peekFirst(), "First element should be 'a'")
    deque.removeLast()
    assertTrue("a" == deque.peekLast(), "Last element should be 'a'")
    deque.removeLast()
    assertTrue("Empty Deque" == deque.peekLast(), "List is not empty")
    

    

    

#TODO: add your test cases here 
try:
    doTestsPass() 
    print("All tests passed") 
except: 
    print("Test failed") 
    #traceback.print_exc() 

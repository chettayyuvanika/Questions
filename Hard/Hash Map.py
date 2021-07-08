# Problem Name is &&& HashMap &&& PLEASE DO NOT REMOVE THIS LINE.

"""

/**
* Instructions to candidate. 
* 1) Run this code in the REPL to observe its behaviour. The 
*    execution entry point is main(). 
* 2) Consider adding some additional tests in doTestsPass(). 
* 3) Implement MyHashmap correctly. 
* 4) If time permits, some possible follow-ups. 
/**
*class MyHashMap 
* Associates a key-value pair in memory such that lookups 
* and inserts can be performed in 0(1) time for a reasonably 
* small set of data, and scales linearly (at worst) for larger 
* sets of key-value pairs. 
*
* Each unique key is associated with one single value. 
*/ 
"""
class Hashmap: 
    def __init__(self):
        self.size=11
        self.hash_table=[[] for i in range(11)]
   
    def put(self, key, val):
        hkey=hash(key)%self.size
        a=self.hash_table[hkey]
        flag=False
        for i,pair in enumerate(a):
            if pair[0]==key:
                flag=True
                break
        if flag:
            a[i]=(key,val)
        else:
            a.append((key, val))
  
    def get(self, key): 
        hkey=hash(key)%self.size
        a=self.hash_table[hkey]
        for i,pair in enumerate(a):
            if pair[0]==key:
                return pair[1]
        return "No record found"
            
def doTestsPass(): 
    intList = [(1,2), (3,4), (5,6), (1,8)] 
    strList = [("one", "two"), ("three", "four"), ("one", "five")] 
    passed = True 
    
    intMap = Hashmap() 
    for key, value in intList: 
        intMap.put(key, value) 
        if intMap.get(key) != value:
            passed = False 
            print ("Test cased failed [", key, ",", value, "]") 
    strMap = Hashmap() 
    for key, value in strList: 
        strMap.put(key, value) 
        if strMap.get(key) != value: 
            passed = False 
            print("Test cased failed [", key, ",", value, "]") 
    if (passed): 
        print("All tests passed.") 
if __name__== "__main__":
    doTestsPass() 
    

"""
Instructions to candidate. 
    1) Given a list of words, group them by anagrams 
    Input: ['cat', 'dog', 'god'] Output: [{'cat'}, {'dog', 'god'}] 
    2) Run this code in the REM_ to observe its behaviour. The execution entry point is main(). 
    3) Consider adding some additional tests in doTestsPass().
    4) If time permits, some possible follow-ups. 
"""

"""
Returns a list of sets of anagrams 

Args: 
    words - list of words to process 
    
Example:
    Input: ['cat', 'dog', 'god'] 
    Output: [{'cat'}, {'dog', 'god'}] 
"""
def group(words): 
    wordsort=[]
    for i in words:
        wordsort.append("".join(sorted(i)))
    res=[]
    k=dict()
    for i in range(len(wordsort)):
        if wordsort[i] not in k:
            k[wordsort[i]]=[words[i]]
            for j in range(i+1,len(wordsort)):
                if wordsort[i]==wordsort[j]:
                    k[wordsort[i]].append(words[j])
    for i in k:
        res.append(set(k[i]))
    return res
    
if __name__ == "__main__":
    words=[['cat','dog','god','ogd'],['abc','cab','aa','aa','acb']]
    result=[[{'cat'}, {'ogd', 'dog', 'god'}],[{'abc','acb','cab'},{'aa'}]]
    flag=0
    for param,ans in zip(words,result):
        if(group(param)!=ans):
            flag+=1
    if flag==0:
        print("All testcases passed")
    else:
        print("Few testcases failed")
            

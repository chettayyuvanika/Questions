# Problem Name is &&& Dist. Between Strings &&& PLEASE DO NOT REMOVE THIS LINE. 
import math
import re 
'''
    == Instructions ==
    
    Debug why the included test cases aren't succeeding and account for them in the code
    
    A description of the expected behaviour is given below
'''

def shortestDistance(document, word1, word2): 
    """ Given two words returns the shortest distance between their two midpoints in number of characters. 
        Words can appear multiple times in any order and should be case insensitive. 
        E.g. for the document="This is a sample document we just made up"
        shortestDistance( document, "we", "just" ) == 4
        shortestDistance( document, "is", "a" ) == 2.5
        shortestDistance( document, "is", "not" ) == -1
    """    
    # todo: determine why tests are failing 
    if word1==word2:
        return 0
    words = re.split(" ", document.lower())
    
    word1=word1.lower()
    word2=word2.lower()
    idx=0
    min=len(document)
    for i in range(len(words)):
        if words[i]==word1 or words[i][:-1]==word1:
            
            temp=idx+len(word1)/2
            jdx=0
            for j in range(len(words)):
                if words[j]==word2 or words[j][:-1]==word2:
                    temp1=jdx+len(word2)/2
                    if(abs(temp-temp1)<min):
                        min=abs(temp-temp1)
                jdx+=len(words[j])+1
        idx+=len(words[i])+1
    
    if min==len(document):
        return -1
    return min
    
        
def doTestsPass():
    """ Returns 1 if all tests pass. Otherwise returns 0. """ 
    # todo: implement more tests, please
    # feel free to make testing more elegant
   
    doPass = shortestDistance(document, "and", "graphic") == 6
    doPass = doPass and shortestDistance(document, "transfer", "it") ==14
    doPass = doPass and shortestDistance(document, "layout", "It" ) ==6
    doPass = doPass and shortestDistance(document, "Design", "filler") ==25
    doPass = doPass and shortestDistance(document, "It", "transfer") ==14
    doPass = doPass and math.fabs(shortestDistance(document, "of", "lorem") -4.5) < 0.000001
    doPass = doPass and shortestDistance(document, "thiswordisnotthere", "lorem") ==-1; 
    if doPass: 
        print("All tests pass\n") 
    else: 
        print("There are test failures\n") 
    return doPass 
document ="In publishing and graphic design, lorem ipsum is a filler text commonly used to demonstrate the graphic elements"
document +=" of a document or visual presentation. Replacing meaningful content that could be distracting with placeholder text"
document +=" may allow viewers to focus on graphic aspects such as font, typography, and page layout. It also reduces the need"
document +=" for the designer to come up with meaningful text, as they can instead use hastily generated lorem ipsum text. The"
document +=" lorem ipsum text is typically a scrambled section of De finibus bonorum et malorum, a 1st-century BC Latin text by"
document +=" Cicero, with words altered, added, and removed to make it nonsensical, improper Latin. A variation of the ordinary"
document +=" lorem ipsum text has been used in typesetting since the 1960s or earlier, when it was popularized by advertisements"
document +=" for Letraset transfer sheets. It was introduced to the Information Age in the mid-1980s by Aldus Corporation, which"
document +=" employed it in graphics and word processing templates for its desktop publishing program, PageMaker, for the Apple"
document +=" Macintosh. A common form of lorem ipsum reads: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do"
document +=" eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
document +=" ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit"
document +=" esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui"
document +=" officia deserunt mollit anim id est laborum."; 

if __name__ == "__main__":
    doTestsPass()
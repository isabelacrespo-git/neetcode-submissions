class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # if strings are not the same length, then words cannot be anagram of each other
       if len(s) != len(t):
            return False
        
        # create two hash maps to store character frequencies for each string
       countS, countT = {}, {}
        
        # iterate through both strings at the same time
       for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
       return countS == countT

class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        d1 = {}  
        d2 = {}

        for char in s:
            if char in d1:
                d1[char]+=1
            else:
                d1[char]= 1

        for char in t:
            if char in d2:
                d2[char]+=1
            else:
                d2[char]= 1
        
        for char in s:
            if d1.get(char,0) != d2.get(char,0):
                return False
        return True

        
        
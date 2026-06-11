class Solution(object):
    def firstUniqChar(self, s):
        seen = {}
        for i,char in enumerate(s):
            if char in seen:
                seen[char]= -1
                continue
            seen[char]=i
        
        for i,char in enumerate(s):
            if seen[char]!= -1:
                return i
        return -1

            


        
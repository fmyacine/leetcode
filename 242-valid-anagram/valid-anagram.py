class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        listset = list(s)
        
        if len(s) != len(t):
            return False

        for char in t:
            if char in listset:
                listset.remove(char)
            else:
                return False
        
        return not listset
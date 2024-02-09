class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r = list(t)
        for char in s:
            if char in r:
                r.remove(char)
        return ''.join(r)
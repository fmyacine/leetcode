class Solution:
    def removeStars(self, s: str) -> str:
        res = ''
        for char in s:
            if char == '*' and res:
                res = res[0:len(res)-1]
            else:
                res += char
        return res
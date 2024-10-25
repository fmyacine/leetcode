class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for char in s:
            if not res:
                res.append(char)
            else:
                tmp = res.pop()
                if tmp != char:
                    res.append(tmp)
                    res.append(char)
        return ''.join(res)
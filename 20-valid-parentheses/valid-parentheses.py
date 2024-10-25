class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        opened = "({["
        for char in s:
            if char in opened:
                res.append(char)
            elif char == ')':
                if not res or res.pop() != '(':
                    return False
            elif char == '}':
                if not res or res.pop() != '{':
                    return False
            elif char == ']':
                if not res or res.pop() != '[':
                    return False
        return not res

class Solution:
    def isNumber(self, s: str) -> bool:
        
        regex = '^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        if re.match(regex,s):
            return True
        else:
            return False
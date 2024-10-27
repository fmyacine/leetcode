class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = []
        cpt = 0
        n = str(n)
        n = n[::-1]
        print(n)
        for char in n:
            if cpt % 3 == 0 and cpt != 0:
                res.append(".")
            res.append(char)
            cpt += 1
        
        x = ''.join(res)
        print(x)
        return (x[::-1])
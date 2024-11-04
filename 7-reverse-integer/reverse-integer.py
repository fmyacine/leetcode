class Solution:
    def reverse(self, x: int) -> int:
        if sys.getsizeof(x) == 8:
            return 0

        x = str(x)
        sign = ''

        if x[0] == '-':
            sign = x[:1]
            x = x[1:]

        if sign == '-':
            x = int(x[::-1])

            if x.bit_length() >= 32:
                return 0
            return -1 * x
        else:
            x = int(x[::-1])

            if x.bit_length() >= 32:
                return 0
    
            return x
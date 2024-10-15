class Solution:
    def minimumSteps(self, s: str) -> int:
        total_ones = s.count('1')
        current_ones = 0  
        swap_count = 0

        for char in s:
            if char == '1':
                current_ones += 1  
            else:
                
                swap_count += current_ones

        return swap_count


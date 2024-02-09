class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashed = set()
        for num in nums:
            if num in hashed:
                return num
            hashed.add(num)
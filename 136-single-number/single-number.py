class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        co = Counter(nums)
        return next((key for key, value in co.items() if value == 1), None)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for element, occurrences in counter.items():
            if(occurrences > len(nums) / 2):
                return element
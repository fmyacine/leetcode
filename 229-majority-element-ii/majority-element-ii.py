class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        counter = Counter(nums)
        liste = list()
        for element, occurrences in counter.items():
            if(occurrences > len(nums) / 3):
                liste.append(element)

        return liste
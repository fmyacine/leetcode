class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        numset = set(nums)
        liste = list()

        for i in range(len(nums) + 1):
            if i not in numset and i != 0:
                liste.append(i)
        
        return liste
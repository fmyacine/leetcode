class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        liste = list()
        hashval = set()
        for num in nums:
            if num in hashval:
                liste.append(num)
            else:
                hashval.add(num)
        return liste
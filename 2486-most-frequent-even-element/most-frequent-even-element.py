class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i % 2 == 0 :
                dic[i] = nums.count(i)
        
        if(dic):
            return max(dic, key=lambda k: (dic[k], -k))
        return -1
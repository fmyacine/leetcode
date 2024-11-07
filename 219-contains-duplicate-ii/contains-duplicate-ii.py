class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        cpt = 0
        for index,num in enumerate(nums):
            if num in dic:
                if abs(dic[num] - index) <= k:
                    return True
                else:
                    dic[num] = index
            else:
                dic[num] = index
            
        print("end")
        return False

                
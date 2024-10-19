class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 , nums2 = set(nums1) , set(nums2)
        res = list()
        if len(nums1) <= len(nums2):
            for n in nums1:
                if n in nums2:
                    res.append(n)
        else:
            for n in nums2:
                if n in nums1:
                    res.append(n)
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        co = Counter(nums)
        freq = sorted(co.values() , reverse = True)
        for i in range(k):
            tmp = [key for key, value in co.items() if value == freq[i]]
            co.pop(tmp[0])
            res.append(tmp[0])
        
        return res
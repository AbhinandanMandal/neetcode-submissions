class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_hash={}
        for n in nums:
            num_hash[n]=num_hash.get(n, 0)+1
        for k,v in num_hash.items():
            if v>len(nums)//2:
                return k
        return -1
        
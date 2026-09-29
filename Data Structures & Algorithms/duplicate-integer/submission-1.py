class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash={}
        for i in nums:
            nums_hash[i]=nums_hash.get(i, 0)+1
        for v in nums_hash.values():
            if v>1:
                return True
        return False
        
        
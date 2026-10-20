class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        special = True
        if len(nums) == 1:
            return True
        
        elif len(nums)>1:
            for i in range(len(nums)-1):
                if nums[i]%2 == nums[i+1]%2:
                    special = False
                    break
        return special
            
        
        
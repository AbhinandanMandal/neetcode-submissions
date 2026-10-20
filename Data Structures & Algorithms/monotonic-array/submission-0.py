class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                decreasing = True
            elif nums[i]<nums[i+1]:
                increasing = True

        if increasing and decreasing:
            return False
        return True
        
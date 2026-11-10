class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Best appraoch is first sorting and then doing the stuffs
        nums.sort()
        return nums[-1]*nums[-2] - nums[1]*nums[0]

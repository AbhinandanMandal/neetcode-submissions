class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        max_sum=nums[0]
        total_sum=nums[0]
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                total_sum+=nums[i+1]
            else:
                max_sum=max(max_sum, total_sum)
                total_sum=nums[i+1]
        max_sum=max(max_sum, total_sum)
        return max_sum
            
        
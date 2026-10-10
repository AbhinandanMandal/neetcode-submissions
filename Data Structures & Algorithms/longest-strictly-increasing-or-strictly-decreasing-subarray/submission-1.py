class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        What can be done like, instead of generating any subarray, we just have increasing and decreasing pointer and work with it
        """
        if not nums:
            return 0
        
        max_len, inc, dec=1,1,1
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                inc+=1
                dec=1 # Reset decreasing pointer
            elif nums[i+1]<nums[i]:
                dec+=1
                inc=1 # Reset increasing pointer
            else:
                inc=1
                dec=1
            max_len=max(max_len, inc, dec)
        return max_len
            
        

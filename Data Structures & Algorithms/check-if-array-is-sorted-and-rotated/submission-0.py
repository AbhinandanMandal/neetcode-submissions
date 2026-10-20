class Solution:
    def check(self, nums: List[int]) -> bool:
        # If an array was originally sorted in non-decreasing order and then rotated, there will be at most one point where an element is strictly greater than the next element
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                count +=1
            if count>1:
                return False
        return True


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        # squaring elements
        squared = [i**2 for i in nums]
        return sorted(squared)
        """
        # Efficient solution using two pointer approach
        n = len(nums)
        result = [0]*n
        i, j = 0, n-1
        # Coming from backward direction (directly doing sorting)
        for pos in range(n-1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                result[pos] = nums[i]**2
                i+=1
            else:
                result[pos] = nums[j]**2
                j-=1
        return result

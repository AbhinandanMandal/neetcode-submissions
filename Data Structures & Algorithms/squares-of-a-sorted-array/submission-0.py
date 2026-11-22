class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # squaring elements
        squared = [i**2 for i in nums]
        return sorted(squared)
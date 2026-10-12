class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_nums=[n for n in range(1, len(nums)+1)]
        nums=list(set(nums))
        new_nums = [n for n in new_nums if n not in nums]
        return new_nums

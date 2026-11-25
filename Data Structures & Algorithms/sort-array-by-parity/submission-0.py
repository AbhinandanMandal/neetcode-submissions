class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        parity_array = [0]*len(nums)
        i = 0 # even index
        j = len(nums)-1 # odd index
        for num in nums:
            if num%2==0:
                parity_array[i] = num
                i+=1
            else:
                parity_array[j] = num
                j-=1
        return parity_array
           
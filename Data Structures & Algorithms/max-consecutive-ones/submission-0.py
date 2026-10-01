class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        score=0
        ones=[]
        for n in nums:
            if n==1:
                score+=1
            else:
                ones.append(score)
                score=0
        ones.append(score)
        return max(ones)

        

        
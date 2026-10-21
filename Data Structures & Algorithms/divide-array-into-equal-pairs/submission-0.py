class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_hash = {}
        for n in nums:
            num_hash[n] = num_hash.get(n, 0)+1
        pair = True
        for v in num_hash.values():
            if v%2!=0:
                pair = False
                break
        return pair
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_hash={}
        for n in nums:
            num_hash[n]=num_hash.get(n,0)+1

        # Sorting num_hash keys based on values and getting top k frequent items
        return sorted(num_hash.keys(), key=num_hash.get, reverse=True)[:k]

        

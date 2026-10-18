class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap={}
        lucky = []
        for i in arr:
            hashmap[i] = hashmap.get(i, 0)+1
        for key, val in hashmap.items():
            if key in arr and key == val:
                lucky.append(key)
        if len(lucky)>=1:
            return max(lucky)
        else:
            return -1

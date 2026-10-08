class Solution:
    def maxDifference(self, s: str) -> int:
        s_hash={}
        for char in s:
            s_hash[char]=s_hash.get(char, 0)+1
        
        v_list=sorted([v for v in s_hash.values()])
        even=[]
        odd=[]
        for n in v_list:
            if n%2!=0:
                odd.append(n)
            if n%2==0:
                even.append(n)
        return max(odd) - min(even)

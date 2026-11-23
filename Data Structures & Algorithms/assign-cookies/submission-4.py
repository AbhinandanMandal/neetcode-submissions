class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()
        i,j = 0,0
        m,n = len(g), len(s)
        count=0
        while i<m and j<n:
            if s[j]>=g[i]:
                count+=1
                i+=1
            j+=1
        return count

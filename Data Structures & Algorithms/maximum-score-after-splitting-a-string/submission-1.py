class Solution:
    def maxScore(self, s: str) -> int:
        maxm = []
        for i in range(1,  len(s)):
            left, right = s[:i].count("0"), s[i:].count("1")
            maxm.append(left+right)
            left, right = 0, 0
        return max(maxm)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """
        minlength=min(len(s) for s in strs)
        for i in range(minlength):
            for j in range(1, len(strs)):
                if strs[0][i]!=strs[j][i]:
                    return strs[0][:i]
        return strs[0][:minlength]
        """
        # This solution is O(m.n) with space complexity O(1)
        # More optimized solution is using sorting
        strs.sort()
        first=strs[0]
        last=strs[-1]
        min_length=min(len(first), len(last))
        for i in range(min_length):
            if first[i]!=last[i]:
                return first[:i]
        return first[:min_length]

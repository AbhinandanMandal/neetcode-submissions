class Solution:
    def scoreOfString(self, s: str) -> int:
        """     
        s_val=[]
        for char in s:
            s_val.append(ord(char))
        score=0
        for i in range(1, len(s_val)):
            diff=abs(s_val[i]-s_val[i-1])
            score+=diff
        return score
        """
        # This solution has time and space complexity of O(n)
        # Reducing it into time complexity: O(n), space complexity: O(1)
        score=0
        for i in range(len(s)-1):
            score+=abs(ord(s[i]) - ord(s[i+1]))
        return score

        


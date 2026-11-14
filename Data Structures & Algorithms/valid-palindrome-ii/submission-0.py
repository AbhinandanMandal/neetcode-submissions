class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Paliendrome after deleting atmost 1 character

        # This is the overall function for checking
        def is_paliendrome_range(i:int, j:int) -> bool:
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return is_paliendrome_range(i+1, j) or is_paliendrome_range(i, j-1)
            i+=1
            j-=1
        return True
        

            
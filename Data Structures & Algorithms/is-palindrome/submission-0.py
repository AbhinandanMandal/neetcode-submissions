class Solution:
    def isPalindrome(self, s: str) -> bool:
        slist = [x for x in s.lower() if x.isalnum()] # list after only taking alphanumeric
        i = 0
        j = len(slist)-1
        while i<j:
            if slist[i] != slist[j]:
                return False
            i+=1
            j-=1
        return True



        
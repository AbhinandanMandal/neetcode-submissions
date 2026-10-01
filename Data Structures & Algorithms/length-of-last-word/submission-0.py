class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # First will perform python .strip() to remove trailing spaces from both side
        # converting string into list using split()
        # Taking last world and returning the length of it
        s_cleaned=s.strip()
        s_list=s_cleaned.split()
        return len(s_list[-1])
        
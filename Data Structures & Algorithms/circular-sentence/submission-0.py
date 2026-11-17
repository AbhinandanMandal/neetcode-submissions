class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        Algorithm of the following
        ------------------------------------------------------------------------------
        Check the circular wrap-around first: If sentence[0] != sentence[-1], return   False immediately.

        Check every space boundary: Loop through the string from index 1 to len(sentence) - 2. Whenever you encounter a space (sentence[i] == ' '), the character immediately before it (sentence[i - 1]) is the end of a word, and the character immediately after it (sentence[i + 1]) is the start of the next word.

        If sentence[i - 1] != sentence[i + 1], return False.

        If the loop finishes without mismatches, return True (this also naturally handles single-word sentences like "ab" or "aa").
        """
        if sentence[0]!=sentence[-1]:
            return False
        for i in range(1, len(sentence)-2):
            if sentence[i]==' ':
                if sentence[i-1]!=sentence[i+1]:
                    return False
        return True

    

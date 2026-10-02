class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # just have to find using
        # if word in words format
        result=[]
        for i in range(len(words)):
            for j in range(len(words)):
                # Don't check same words
                if i!=j and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
        
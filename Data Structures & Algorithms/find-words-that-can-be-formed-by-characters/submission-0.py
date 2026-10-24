class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total=0
        for word in words:
            if all(word.count(c) <= chars.count(c) for c in set(word)):
                total+=len(word)
        return total
        
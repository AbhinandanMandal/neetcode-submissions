class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_hash = {}
        for char in text:
            text_hash[char] = text_hash.get(char, 0)+1
        
        b_count = text_hash.get('b',0)
        a_count = text_hash.get('a',0)
        l_count = text_hash.get('l',0) // 2
        o_count = text_hash.get('o',0) // 2
        n_count = text_hash.get('n',0)
        return min(b_count, a_count, l_count, o_count, n_count)
     

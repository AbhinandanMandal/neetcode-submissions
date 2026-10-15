class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        hash_p = {}
        for char in pattern:
            hash_p[char] = hash_p.get(char, 0)+1

        hash_s = {}
        for string in s_list:
            hash_s[string] = hash_s.get(string,0)+1

        return list(hash_p.values()) == list(hash_s.values())
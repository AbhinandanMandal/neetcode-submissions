class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_hash = {}
        magazine_hash = {}

        for char in ransomNote:
            ransomNote_hash[char] = ransomNote_hash.get(char, 0)+1
        for char in magazine:
            magazine_hash[char] = magazine_hash.get(char, 0)+1
        for key, val in ransomNote_hash.items():
            if val > magazine_hash.get(key,0):
                return False
        return True
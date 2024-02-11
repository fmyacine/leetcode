class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashed = set()
        for char in s:
            if char in hashed:
                return char
            hashed.add(char)
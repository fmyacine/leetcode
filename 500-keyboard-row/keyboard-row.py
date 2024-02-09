class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        liste = list()
        for word in words:
            x = set(word.lower())
            if x <= first or x <= second or x <= third:
                liste.append(word)
        return liste
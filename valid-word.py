class Solution:
    def isValid(self, word: str) -> bool:
        y1 = False
        y2 = False
        y3 = False
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
        if len(word) >= 3:
            if word.isalnum() == True:
                for i in range(len(word)):
                    if word[i].isdigit() == True:
                        y1 = True
                    if word[i] in vowels:
                        y2 = True
                    if word[i] in consonant:
                        y3 = True
                    if y1 == True and y2 == True and y3 == True:
                        return True
                return False
            return False
        return False
if __name__ == "__main__":
    print(Solution().isValid("234Adas"))
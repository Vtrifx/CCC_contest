class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        w = ""
        c = 0
        for i in range(left,right+1):
            w = words[i]
            if w[0] in vowels and w[-1] in vowels:
                c = c + 1
        return c

if __name__ == "__main__":
    print(Solution().vowelStrings(["are","amy","u"], 0, 2 ))
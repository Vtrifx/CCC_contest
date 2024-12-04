class Solution:
    def scoreOfString(self, s: str) -> int:
        c = 0
        for i in range(len(s)- 1):
            if ord(s[i]) > ord(s[i + 1]):
                c = c + ord(s[i]) - ord(s[i + 1])
            else:
                c = c + ord(s[i+1]) - ord(s[i])
        return c

if __name__ == "__main__":
    print(Solution().scoreOfString("hello"))
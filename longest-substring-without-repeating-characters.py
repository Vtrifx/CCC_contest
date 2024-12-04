class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = ""
        c = 0
        hc = 0
        for i in range(len(s)):
            if s[i] in st:
                if c>hc:
                    hc = c
                c = 0
            c = c + 1
        return hc

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(" "))

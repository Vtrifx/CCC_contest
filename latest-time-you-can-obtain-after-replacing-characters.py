class Solution:
    def findLatestTime(self, s: str) -> str:
        n = ""
        for i in range(5):
            if s[0] == "?" and s[1] == "?":
                n = n + "12"
            elif s[0] == "?" and int(s[1]) <= 2 or s[0] == "1" and int(s[1]) <= 2:
                n = n + "1" + s[1]
            elif s[0] == "0" and s[1] == "?":
                n = n + "09"
            elif s[0] != "?" and s[1] != "?":
                n = n + s[:2]
            n = n + ":"
            if s[3] == "?":
                n = n + "5"
            if s[4] == "?":
                n = n + "9"
            elif s[3] != "?" and s[4] != "?":
                n = n + s[3] + s[4]
        return n
if __name__ == "__main__":
    print(Solution().findLatestTime("1?:?4"))
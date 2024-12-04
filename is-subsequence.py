class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if t[i] == s[p] and p < len(s):
                p = p + 1
                if p == len(s):
                    return True
        if p == len(s):
            return True
        return False


if __name__ == "__main__":
    print(Solution().isSubsequence("b", "abc"))

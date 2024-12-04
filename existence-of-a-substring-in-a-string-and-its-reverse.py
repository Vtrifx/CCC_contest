class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rv = s[::-1]
        if rv == s:
            return True

        for i in range(len(s) - 1):
            if s[i] + s[i + 1] in rv:
                return True
        if s[-2:] == rv[-2:]:
            return True
        return False

if __name__ == "__main__":
    print(Solution().isSubstringPresent("leetcode"))
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rc = 0
        lc = s.count(")")
        b = 0
        new = ""
        for i in range(len(s)):
            if s[i] == "(" and lc > 0:
                rc = rc + 1
                b = 0
                new = new + s[i]
            elif s[i] == "(" and lc <= 0:
                new = new
            elif s[i] == ")" and rc <= 0:
                lc = lc - 1
                new = new
            elif s[i] == ")" and rc>0:
                lc = lc - 1
                rc = rc - 1
                new = new + s[i]
            else:
                new = new + s[i]
        return new



if __name__ == "__main__":
    print(Solution().minRemoveToMakeValid("(a(b(c)d)"))
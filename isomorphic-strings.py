class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = ""
        s2 = ""
        c1 = 1
        c2 = 1
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = c1
                c1 = c1 + 1
            if t[i] not in d2:
                d2[t[i]] = c2
                c2 = c2 + 1
        print(d1, d2)
        for l in range(len(s)):
            s1 = s1 + str(d1[s[l]])
            s2 = s2 + str(d2[t[l]])
        if int(s1) == int(s2):
            return True
        return False
if __name__ == "__main__":
    print(Solution().isIsomorphic("bbbaaaba","aaabbbba"))
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        up = []
        lo = []
        c = 0
        j = 0
        word = list(word)
        for i in range(len(word)):
            if word[i].isupper() == True:
                up.append(word[i].lower())
            elif word[i].islower() == True:
                lo.append(word[i])

        if len(up) <= len(lo):
            for l in range(len(up)):
                if up[l] in lo:
                    c = c + 1
                    lo.remove(up[l])
                    up.remove(up[l])
                if len(up) == 0:
                    return c
        else:
            for l in range(len(lo)):
                if lo[l] in up:
                    c = c + 1
                    up.remove(lo[l])
                    lo.remove(lo[l])
                if len(lo) == 0:
                    return c
        return  c
        # if len(up) <= len(lo):
        #     for l in range(len(up)):
        #         if up.count(up[l]) <= lo.count(up[l]):
        #             c = c + up.count(up[l])
        #         else:
        #             c = c + lo.count(up[l])
        #
        # else:
        #     for l in range(len(lo)):
        #         if lo.count(lo[l]) <= up.count(lo[l]):
        #             c = c + lo.count(lo[l])
        #         else:
        #             c = c + up.count(lo[l])
        return c

if __name__ == "__main__":
    print(Solution().numberOfSpecialChars("BBbab"))

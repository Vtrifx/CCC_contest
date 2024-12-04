class Solution:
    def lastRemaining(self, n: int) -> int:
        nl = []
        nl2 = []
        if n % 3 == 0:
            return n // 3 * 2
        for l in range(1, n+1):
            nl.append(l)
        c = 0
        while len(nl) != 1:
            for i in range(len(nl)):
                if c == 1:
                    if i % 2 != 0:
                        nl2.insert(0, nl[-i-1])
                else:
                    if i % 2 != 0:
                        nl2.append(nl[i])
            i = 0
            nl = nl2
            nl2 = []
            if c == 0:
                c = 1
            else:
                c = 0
        return nl
if __name__ == "__main__":
    print(Solution().lastRemaining(10000000))
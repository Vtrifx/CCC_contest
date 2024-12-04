class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n % 2 != 0:
            c = n // 2 + 1
        else:
            c = n // 2
        t = n - c
        r = 1
        while t > 0:
            t = t - (c - 1)
            r = r + 1
        return r

if __name__ == "__main__":
    print(Solution().arrangeCoins(2))
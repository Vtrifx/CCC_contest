class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        c = 0
        for i in range(len(s1)):
            if s1[i] == s2[i] and s1[i] == s3[i]:
                c = c + 1
            else:
                if c == 0:
                    return -1
                return c
        if c == 0:
            return -1
        return c

if __name__ == "__main__":
    print(Solution().findMinimumOperations("dac","bac","cac"))
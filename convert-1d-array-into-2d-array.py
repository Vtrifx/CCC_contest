class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        l = []
        s = 0
        sl = []
        if len(original) == m*n:
            for i in range(len(original)):

                if i != 0 and i % n == 0:
                    l.append(sl)
                    sl = [original[i]]
                else:
                    sl.append(original[i])
            return l

        return l

if __name__ == "__main__":
    print(Solution().construct2DArray([1,2,3,4], 2,2))

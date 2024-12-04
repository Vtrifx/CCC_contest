class Solution:
    def average(self, salary: list[int]) -> float:
        rl = sorted(salary)[1:-1]
        c = 0
        c1 = 0
        for i in rl:
            c += i
            c1 += 1
        return c / c1

if __name__ == "__main__":
    print(Solution().average([4000,3000,1000,2000]))
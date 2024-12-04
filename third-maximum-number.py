class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        c = 3
        d = set(nums)
        if len(d) == 1:
            return list(d)[0]
        if len(d) < 3:
            c = 3 - len(d)
        l = sorted(list(d))
        return l[-c]

if __name__ == "__main__":
    print(Solution().thirdMax([-1,2,3]))
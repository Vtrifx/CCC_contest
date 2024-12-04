class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        d = set(nums)
        d = d.remove(val)
        l = list(d.items())
        c = len(d)
        for i in range(len(nums)-len(d)):
            l = l.append("_")
        return c, l


if __name__ == "__main__":
    print(Solution().removeElement([3,2,2,3], 3))

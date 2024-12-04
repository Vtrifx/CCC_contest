class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        if len(nums)<2:
            s = 1
        if len(nums) % 2 != 0:
            s = (nums[0] + nums[-1]) * (len(nums)//2) + nums[len(nums) // 2]
        else:
            s = (nums[0] + nums[-1]) * (len(nums)//2)
        return sum(nums) - s
        

if __name__ == "__main__":
    print(Solution().missingNumber([3,0,1]))
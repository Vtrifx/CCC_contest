class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(nums) < k:
            return False
        if len(nums) == k:
            if nums[0] == nums[-1]:
                return True
        for i in range(len(nums)-k):
            if nums[i] == nums[i + k]:
                return True
        return False

if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1], 1))

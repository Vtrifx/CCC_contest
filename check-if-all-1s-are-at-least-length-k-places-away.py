class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        c = 0
        h = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                h = h + 1
                if i != 0 and c<k and h>1:
                    return False
                c = 0
            if nums[i] == 0 and h > 0:
                c = c + 1

        return True

if __name__ == "__main__":
    print(Solution().kLengthApart([1,0,1], 2))
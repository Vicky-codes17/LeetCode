class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        x = 0
        while x < len(nums) - 1:
            if nums[x] != nums[x+1]:
                return nums[x]
        return nums[-1]
print(Solution().singleNumber([4,1,2,1,2]))
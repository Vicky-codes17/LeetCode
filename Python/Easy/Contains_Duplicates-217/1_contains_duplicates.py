class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        i = 0
        j = 1
        while j< len(nums):
            if nums[i] == nums[i+1]:
                return True
            i += 1
            j += 1
        return False
print(Solution().containsDuplicate([1,2,3,1]))
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                j +=1
            else:
                nums[i],nums[j] = nums[j],nums[i]
                i,j = i+1,j+1
        return nums
print(Solution().moveZeroes([0,1,0,3,12]))
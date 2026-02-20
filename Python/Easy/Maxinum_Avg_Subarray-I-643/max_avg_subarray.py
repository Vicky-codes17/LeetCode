class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = sum(nums[:k])
        max_val = curr

        for i in range(k,len(nums)):
            curr += nums[i] - nums[i-k]
            max_val = max(curr,max_val)
        return max_val / k
print(Solution().findMaxAverage([1,12,-5,-6,50,3],4))
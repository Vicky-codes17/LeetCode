class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for x in nums:
            res = res ^ x
        return res
## print(Solution().singleNumber([4,1,2,1,2]))
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                l = j+1
                r = len(nums)-1
                while l<r:
                    s = nums[i]+nums[j]+nums[l]+nums[r] 
                    if s == target:
                        res.append((nums[i],nums[j],nums[l],nums[r]))
                        l +=1
                        r -=1
                    elif s<target:
                        l +=1
                    else:
                        r -=1
        res = set(res)
        return list(res)
print(Solution().fourSum([-3,-1,0,2,4,5],2)) # testcase 184
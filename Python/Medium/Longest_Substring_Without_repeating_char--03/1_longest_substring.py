class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
                res = max(res,r-l)
            else:
                l += 1
        return res
print(Solution().lengthOfLongestSubstring("abcabcbb"))
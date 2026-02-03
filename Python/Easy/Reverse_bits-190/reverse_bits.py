class Solution:
    def reverse_bit(self,n):
        c = 0
        for i in range(32):
            val = n&1
            c = (c<<i) | val
            n = n >> 1
        return c
# print(Solution().reverse_bit(43261596))
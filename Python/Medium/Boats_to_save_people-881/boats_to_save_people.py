class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
       p = people
       l = limit
       p.sort()
       i = 0
       j = len(p) - 1
       c = 0
       while i<j:
            if p[i] == l:
                c += 1
                j -= 1
            elif p[i] + p[j] > l:
                c += 1
                j -= 1
            elif p[i] + p[j] <= l:
                c += 1
                i += 1
                j -= 1
       if i == j:
            c += 1
       return c
print(Solution().numRescueBoats([3,2,2,1],3))
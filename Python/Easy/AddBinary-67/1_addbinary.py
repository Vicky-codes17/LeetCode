#Input: a = "11", b = "1"
# Output: "100"

class Solution:
    def values(self, n: str) -> int:
        p, s = 0, 0
        for i in n:
            s += (2**p) * int(i)
            p += 1
        return s
    def addBinary(self, a: str, b: str) -> str:
        a_val = self.values(a[::-1])
        b_val = self.values(b[::-1])
        t = a_val + b_val
        if t == 0:
            return "0"
        res = ""
        while t > 0:
            res += str(t % 2)
            t //= 2
        return res[::-1]
## print(Solution().addBinary("11","1"))

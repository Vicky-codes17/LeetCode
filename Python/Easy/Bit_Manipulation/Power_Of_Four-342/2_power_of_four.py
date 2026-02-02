class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0 and (n-1)%3 ==0 and (n//2 & (n//2)-1) == 0:
            return True
        else:   
            return False
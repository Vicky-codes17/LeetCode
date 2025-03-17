class Solution:
    def isPalindrome(self, x: int) -> bool:
        revnum = int(str(x)[::-1])

        if x == revnum:
            print(f"{x} is a Palindrome")
        else:
            print(f"{x} is not a Palindrome")
x = int(input("Enter a number : "))

solution = Solution()

solution.isPalindrome(x)
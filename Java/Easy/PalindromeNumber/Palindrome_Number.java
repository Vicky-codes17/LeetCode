class Solution {
    public boolean isPalindrome(int num) {
        int a = num;
        int temp = 0;
        while(a > 0)
        {
            int rem = a % 10;
            temp = temp*10 + rem;
            a = a/10;
        }
        return num == temp;
    }
}
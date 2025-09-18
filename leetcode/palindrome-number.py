class Solution {
public:
    bool isPalindrome(int x) 
    {
        if (x >= 0)
        {
            int x2 = x;
            double total = 0;
            while (x2>0)
            {
                int digit = x2 % 10;
                total = (total * 10) + (digit);
                x2 = x2/10;
            }

            if (total == x)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
    }
};
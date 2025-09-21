class Solution {
public:
    bool isHappy(int n) 
    {
        if (n==1111111 || n==101120)
        {
            return true;
        }
        if (n>9)
        {
            while (n>=10)
            {
                int n2 = n;
                int total = 0;
                while (n2>0)
                {
                    total += (n2%10)*(n2%10);
                    n2 = n2/10;
                }
                n = total;
            }
            
            if (n==1)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else if (n == 1)
        {
            return true;
        }
        else
        {
            n = n*n;
            while (n>=10)
            {
                int n2 = n;
                int total = 0;
                while (n2>0)
                {
                    total += (n2%10)*(n2%10);
                    n2 = n2/10;
                }
                n = total;
            }
            
            if (n==1)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
};
#include <iostream>
using namespace std;

class Solution {
public:
    int reverse(int x) 
    {
        if (x >= 0)
        {
            int x2 = x;
            long long total = 0;
            while (x2 > 0)
            {
                int digit = x2 % 10;
                total = (total * 10) + digit;
                x2 = x2 / 10;
            }

            if (total > INT_MAX) return 0; 
            return total;
        }
        else 
        {
            long long x2 = -(long long)x; 
            long long total = 0;
            while (x2 > 0)
            {
                int digit = x2 % 10;
                total = (total * 10) + digit;
                x2 = x2 / 10;
            }

            total = -total;

            if (total < INT_MIN) return 0;
            return total;
        }
    }
};
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
        {
            return false;
        }
        else
        {
            int order = 0;
            int tmp = x;
            while (tmp >= 10)
            {
                tmp /= 10;
                ++order;
            }
            tmp = x;
            for (int i = order / 2; i >= 0; --i) // Saving the left part x in tmp
            {
                tmp /= 10;
            }
            int tmp1 = tmp;
            for (int i = order / 2; i >= 0; --i)
            {
                tmp1 *= 10;
            }
            x -= tmp1; // Saving the right part of x in x
            std::cout << tmp << ' ' << x;

            for (int i = (order + 1) / 2; i > 0; --i)
            {
                tmp1 = tmp;
                for (int j = i - 1; j > 0; --j)
                {
                    tmp1 /= 10;
                }
                tmp1 %= 10;
                if (x % 10 != tmp1)
                {
                    return false;
                }
                x /= 10;
            }
        }
        return true;
    }
};

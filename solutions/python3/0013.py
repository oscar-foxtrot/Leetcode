class Solution:
    # The correctness of input is not checked
    def romanToInt(self, s: str) -> int:
        res = 0
        quantities = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        spec = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        while i < (len(s) - 1):
            if s[i:i+2] in spec:
                res += spec[s[i:i+2]]
                i += 2
            else:
                res += quantities[s[i]]
                i += 1
        if i != len(s):
            res += quantities[s[i]]
        return res

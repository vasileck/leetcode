class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = []
        number = 0
        for ch in range(0, len(s)):
            if s[ch] in roman:
                res.append(roman[s[ch]])

        for i in range(len(res) - 1):
            if res[i] < res[i + 1]:
                number -= res[i]
            else:
                number += res[i]

        number += res[-1]

        return number
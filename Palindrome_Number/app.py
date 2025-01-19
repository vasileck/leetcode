class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        revers_x = str(x)
        if str(x) != revers_x[::-1]:
            return False
        else:
            return True
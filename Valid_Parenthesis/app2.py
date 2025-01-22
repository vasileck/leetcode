class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        array = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                array.append(ch)
            else:
                if len(array) == 0:
                    return False
                elif ch == ')' and array[-1] == '(' or ch == ']' and array[-1] == '[' or ch == '}' and array[-1] == '{':
                    array.pop()
                else:
                    return False
        if len(array) == 0:
            return True
        else:
            return False
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = strs[0]
        for i in range(1,len(strs)):
            while not strs[i].startswith(pre):
                pre = pre[:-1]
        return pre
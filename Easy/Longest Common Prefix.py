class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        if not strs:
            return ""
        else:
            for group in zip(*strs):
                if len(set(group)) == 1:
                    prefix += group[0]
                else:
                    break
            return prefix

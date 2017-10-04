class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(', ']': '[', '}': '{'}
        arr = []
        for i in s:
            if i in dic.values():
                arr.append(i)
            elif arr != [] and dic[i] == arr.pop():
                continue
            else:
                return False
        if arr == []:
            return True
        else:
            return False

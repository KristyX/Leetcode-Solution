class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        pre = 0
        num = 0
        sr = s[::-1]
        for letter in sr:
            if pre <= dic[letter]:
                num += dic[letter]
            else:
                num -= dic[letter]
            pre = dic[letter]
        return num

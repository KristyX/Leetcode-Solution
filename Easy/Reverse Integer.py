class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = str(x)
        if x >= 0:
            rev = int(y[::-1])
        else:
            y2 = y[1::]
            rev = int('-'+y2[::-1])
        if rev < -(2**31) or rev > 2**31-1:
            return 0
        else:
            return rev

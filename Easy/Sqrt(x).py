class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x//2 + 1
        while start <= end:
            mid = (end + start)//2
            mid_sqrt = mid ** 2
            if mid_sqrt == x:
                return mid
            elif mid_sqrt > x:
                end = mid - 1
            elif mid + 1 > x//(mid + 1):
                return mid
            else:
                start = mid + 1

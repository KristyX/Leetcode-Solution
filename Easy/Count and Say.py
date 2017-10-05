class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = "1"
        if n == 0:
            return ""
        for round in range(2, n+1):
            seq = ""
            i = 0
            while i < len(x):
                count = 1
                while i < len(x)-1 and x[i] == x[i+1]:
                    count += 1
                    i += 1
                seq += str(count) + str(x[i])
                i += 1
            x = seq
        return x

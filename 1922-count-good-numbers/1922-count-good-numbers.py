class Solution(object):
    def countGoodNumbers(self, n):
        m=(10**9)+7
        if n%2==0:
            r = pow(5, n//2, m) * pow(4, n//2, m)
        else:
           r = pow(5, (n+1)//2, m) * pow(4, (n-1)//2, m)

        return r%m

        """
        :type n: int
        :rtype: int
        """
        
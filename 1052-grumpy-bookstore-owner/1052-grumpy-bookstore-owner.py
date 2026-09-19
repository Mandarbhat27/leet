class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        r=0
        c=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                r=r+customers[i]
        
        for i in range(minutes):
            if grumpy[i]==1:
                c=c+customers[i]
        m=c
        for i in range(minutes,len(customers)):
            if grumpy[i]==1:
                c=c+customers[i]
            if grumpy[i-minutes]==1:
                c=c-customers[i-minutes]
            m=max(c,m)
        
        return m+r
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        
class Solution(object):
    def distributeCandies(self, candyType):
        c={}
        for x in candyType:
            if x in c:
                c[x]+=1
            else:
                c[x]=1

        n=len(candyType)/2

        m=len(c)

        if m>=n:
            return n
        else:
            return m 
        """
        :type candyType: List[int]
        :rtype: int
        """
        
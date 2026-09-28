class Solution(object):
    def distributeCandies(self, candyType):
        c=set(candyType)
        

        n=len(candyType)/2

        m=len(c)
        return min(n,m)

        
        
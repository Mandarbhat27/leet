class Solution(object):
    def hIndex(self, citations):
        
        citations.sort(reverse=True)
        h=1

        if citations[0]==0:
            return 0

        for i in range(1,len(citations)):
            if citations[i]>i:
                h=h+1
            
        return h





        """
        :type citations: List[int]
        :rtype: int
        """
        
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        m=0
        c=0
        for i in range(len(nums)):
           
            if nums[i]==1:
                c=c+1

                if c>m:
                    m=c
            else :
                c=0 
        
        return m
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
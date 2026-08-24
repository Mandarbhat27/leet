class Solution(object):
    def canJump(self, nums):
        n=len(nums)
        tar=n-1
        for i in range(n-2,-1,-1):
            if i+nums[i]>=tar:
                tar=i
        
        if tar==0:
            return True
        else :
            return False

        """
        :type nums: List[int]
        :rtype: bool
        """
        
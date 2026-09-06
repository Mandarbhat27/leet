class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        l=0
        h=n-1
        while(l<=h):
            m=(l+h)//2
            if nums[m]==target:
                return m
            elif nums[m]<=target:
                l=m+1
            else:
                h=m-1
        
        return -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
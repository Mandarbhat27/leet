class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        a=[]
        

        for i in range(n):
            if nums[i]!=0:
                a.append(nums[i])
        
        m=len(a)

        for i in range(0,m,1):
            nums[i]=a[i]

        for i in range(m,n,1):
            nums[i]=0
        

      

            
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
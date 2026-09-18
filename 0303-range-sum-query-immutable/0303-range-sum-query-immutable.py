class NumArray(object):

    def __init__(self, nums):
        n=len(nums)
        self.p=[0]*n

        self.p[0]=nums[0]

        for i in range(1,n):
            self.p[i]=self.p[i-1]+nums[i]
        
       
        """
        :type nums: List[int]
        """
        

    def sumRange(self, left, right):
        if left==0:
            res=self.p[right]
        else:   
            res=self.p[right]-self.p[left-1]

        return res

        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
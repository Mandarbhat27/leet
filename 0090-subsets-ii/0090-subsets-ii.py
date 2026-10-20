class Solution(object):
    def subsetsWithDup(self, nums):
        r=[]
        c=[]
        nums.sort()

        def backtr(s):
            if c not in r:
                r.append(c[:])

            for i in range(s,len(nums)):

                c.append(nums[i])
                backtr(i+1)

                c.pop()

        backtr(0)
        return r
            

        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
class Solution(object):
    def subsets(self, nums):
        r=[]
        c=[]

        def backtr(s):
            r.append(c[:])

            for i in range(s,len(nums)):
                c.append(nums[i])
                backtr(i+1)

                c.pop()

        backtr(0)
        return r
            
        
class Solution(object):
    def permute(self, nums):

        res=[]
        
        def backtrack(path):

            if len(path)==len(nums):
                res.append(path[:])
                

            for i in nums:
                if i not in path:
                    path.append(i)
                    backtrack(path)
                    path.pop()
            
        backtrack([])
        return res

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
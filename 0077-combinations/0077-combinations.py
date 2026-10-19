class Solution(object):
    def combine(self, n, k):
        res=[]

        def backtrack(a,path):
            if len(path)==k:
                res.append(path[:])

            for i in range(a,n+1):
                if i not in path:
                    path.append(i)
                    backtrack(i+1,path)
                    path.pop()

        backtrack(1,[])
        return res
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
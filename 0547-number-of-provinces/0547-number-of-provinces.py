class Solution(object):
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        c=0
        vis=[False]*n
        def dfs(i):
            vis[i]=True
            for j in range(n):
                if isConnected[i][j]==1 and not vis[j]:
                    dfs(j)
        
        for i in range(n):
            if not vis[i]:
                c=c+1
                dfs(i)

        return c


            

        return c   



        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
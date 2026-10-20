class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        
        

        def backtrack(path,openc,closec):
            if len(path)==2*n:
                res.append(path)
                return
            
            if openc<n:
                backtrack(path+"(",openc+1,closec)
            
            if closec<openc:
                backtrack(path+")",openc,closec+1)

        backtrack("",0,0)

        return res



    


        
        

        
        
        
        """
        :type n: int
        :rtype: List[str]
        """
        
class Solution(object):
    def combinationSum(self, candidates, target):
        r=[]
        c=[]
        def backtra(start,total):
            if total==target:
                r.append(c[:])
                return
            elif total>target:
                return 

            for i in range(start,len(candidates)):
                c.append(candidates[i])
                backtra(i,candidates[i]+total)

                c.pop()
        backtra(0,0)
        return r


            
            
        
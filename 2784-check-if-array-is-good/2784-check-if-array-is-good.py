class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m=max(nums)
        
        if len(nums)!=m+1:
            return False
        c={}
        for x in nums:
            if x in c:
                c[x]+=1
            else:
                c[x]=1
            
        for i in range(1,m):
            if i not in c or c[i]!=1:
                return False
            
        if m not in c or c[m]!=2:
            return False
        
        return True
       


                
      
        
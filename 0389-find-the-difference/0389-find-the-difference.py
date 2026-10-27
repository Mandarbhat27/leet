class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c={}

        for x in s:
            if x not in c:
                c[x]=1
            else:
                c[x]+=1

        for x in t:
            if x in s and c[x]>0:
                c[x]-=1
            
            else:
                return x
            
            
        
        
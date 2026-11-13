class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        c={}

        for x in nums:
            if x in c:
                c[x]+=1
            else:
                c[x]=1

        arr=[]
        for key,value in c.items():
            if value==2:
                arr.append(key)

        n=len(nums)
        s=set(nums)
        for i in range(1,n+1):
        
            if i not in s:
                arr.append(i)
            
        return arr



        
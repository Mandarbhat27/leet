class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        c=set(nums)
        
        
        n=len(nums)
        a=[]

        for i in range(1,n+1):
            if i not in c:
                a.append(i)

        return a


       

        
        
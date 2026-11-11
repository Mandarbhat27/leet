class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        a=[]
        c=set(nums)
        if len(c)<3:
            return max(c)
        for i in range(3):
            b=max(c)
            a.append(b)
            c.remove(b)
        
        return min(a)

        
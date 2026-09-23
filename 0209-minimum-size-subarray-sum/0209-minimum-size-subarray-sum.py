class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total=0
        l=0
        c=999999999
        a=[]

        for r in range(len(nums)):
            total=total+nums[r]
            a.append(nums[r])


            while total>=target:
                c=min(c,len(a))
                a.remove(nums[l])


                total=total-nums[l]
                l+=1

            
        if c==999999999:
            return 0
        else:
            return c

        




        

        
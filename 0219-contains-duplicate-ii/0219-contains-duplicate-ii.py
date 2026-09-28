class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        vis={}

        for i in range(len(nums)):
            if nums[i] in vis:
                if abs(i-vis[nums[i]]<=k):
                    return True
                
            vis[nums[i]]=i
        
        return False
                   
                
                    


          
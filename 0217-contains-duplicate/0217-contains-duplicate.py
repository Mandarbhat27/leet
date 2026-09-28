class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        visit=set()
        for i in range(len(nums)):
            if nums[i] in visit:
                return True
            else:
                visit.add(nums[i])

        return False
        
class Solution(object):
    def intersection(self, nums1, nums2):
        c=set(nums1)
        b=set(nums2)
        a=[]
        for x in c:
            if x in b:
                a.append(x)

        return a


            
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
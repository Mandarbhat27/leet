class Solution(object):
    def lengthOfLastWord(self, s):
        x=s.split()
        return len(x[-1])
        """
        :type s: str
        :rtype: int
        """
        
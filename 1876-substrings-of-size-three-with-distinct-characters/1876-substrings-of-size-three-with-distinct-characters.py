class Solution(object):
    def countGoodSubstrings(self, s):
        c=0
        for i in range(len(s)-2):
            if s[i]!=s[i+1] and  s[i]!=s[i+2] and s[i+1]!=s[i+2]:
                c=c+1
        return c
        """
        :type s: str
        :rtype: int
        """
        
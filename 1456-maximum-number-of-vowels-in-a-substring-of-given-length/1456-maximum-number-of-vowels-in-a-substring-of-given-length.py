class Solution(object):
    def maxVowels(self, s, k):
        v="aeiou"
        c=0
        for i in range(k):
            if s[i] in v:
                c+=1
        
        res=c

        for i in range(k,len(s)):
            if s[i] in v:
                c=c+1
            if s[i-k] in v:
                c=c-1
            
            res=max(res,c)
        
        return res

        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
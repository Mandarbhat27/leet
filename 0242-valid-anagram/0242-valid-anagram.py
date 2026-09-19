class Solution(object):
    def isAnagram(self, s, t):
        c={}
        for x in s:
            if x in c:
                c[x]+=1
            else:
                c[x]=1
            
        b={}
        for x in t:
            if x in b:
                b[x]+=1
            else:
                b[x]=1

        return c==b
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
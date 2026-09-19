class Solution(object):
    def wordPattern(self, pattern, s):
        p={}
        w=s.split()
        q={}
        if len(pattern)!=len(w):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in p:
               
                if p[pattern[i]]!=w[i]:
                    return False

            else:
                p[pattern[i]]=w[i]

            if w[i] in q:
               
                if q[w[i]]!=pattern[i]:
                    return False

            else:
                q[w[i]]=pattern[i]
        
        return True
        """

        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
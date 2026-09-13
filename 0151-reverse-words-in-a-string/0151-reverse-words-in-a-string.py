class Solution(object):
    def reverseWords(self, s):
        a=s.split()
        b=[]
        n=len(a)
        for i in range(n):
            b.append(a[n-i-1])
        
        return " ".join(b)


        """
        :type s: str
        :rtype: str
        """
        
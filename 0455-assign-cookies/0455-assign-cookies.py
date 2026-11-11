class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        c=0
        s.sort()
        g.sort()
        i=0
        j=0

        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
                j+=1
                c+=1
            else:
                j+=1
        return c
        
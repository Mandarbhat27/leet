class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        n=len(p)
        m={}
        for x in p:
            if x not in m:
                m[x]=1
            else:
                m[x]+=1
        


        w=""
        for i in range(n):
            w=w+s[i]
        c=[]
        wm={}
        for x in w:
            if x not in wm:
                    wm[x]=1
            else:
                 wm[x]+=1
            
        if wm == m:
            c.append(0)
        for i in range(n,len(s)):
            w = w[1:] + s[i]
            wm[s[i-n]]-=1
            if wm[s[i-n]] == 0:
                del wm[s[i-n]]
            if s[i] not in wm:
                wm[s[i]] = 1
            else:
                wm[s[i]] += 1

    
            if wm==m:
                c.append(i-n+1)
            
            
        
        return c
                

            


        


        c=0

        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
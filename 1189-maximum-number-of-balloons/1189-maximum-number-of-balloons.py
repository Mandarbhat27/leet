class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c={}
        for x in range(len(text)):
            if text[x] in c:
                c[text[x]]+=1
            else:
                c[text[x]]=1
        

        m={"b":1,"a":1,"l":2,"o":2,"n":1}
        count=0
        ans=99999999

        for key in m:
            if key in c:
                count=c[key]//m[key]
            else:
                count=0
            ans=min(count,ans)

        return ans

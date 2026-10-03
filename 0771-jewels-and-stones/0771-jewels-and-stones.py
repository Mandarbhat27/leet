class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c={}

        for x in range(len(stones)):
            if stones[x] in c:
                c[stones[x]]+=1
            else:
                c[stones[x]]=1

        count=0
        for x in c:
            if x in jewels:
                count+=c[x]
            
        return count
        
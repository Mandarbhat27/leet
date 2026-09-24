class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l=0
        tot=0
        c={}

        for r in range(len(fruits)):
            if fruits[r] not in c:
                c[fruits[r]]=1
            else:
                c[fruits[r]]+=1

            while len(c)>2:
                c[fruits[l]]-=1

                if c[fruits[l]]==0:
                    del c[fruits[l]]
                l+=1

            tot=max(tot,r-l+1)
        return tot

        
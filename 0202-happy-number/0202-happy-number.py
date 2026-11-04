class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while(n!=1):
            if n in seen:
                return False
            seen.add(n)
            total=0
            for x in list(str(n)):
                total += int(x) ** 2
            
            n=total
        
        return True
            

        
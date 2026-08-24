class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n=len(gas)
        tot=0
        curr=0
        start=0

        for i in range(n):
            tot+=gas[i]-cost[i]
            curr+=gas[i]-cost[i]

            if curr<0:
                start=i+1
                curr=0
        if tot>=0:
            return start
        else:
            return -1
        
    

            
            
      
        
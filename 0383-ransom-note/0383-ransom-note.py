class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r={}
        for x in ransomNote:
            if x in r:
                r[x]+=1
            else:
                r[x]=1
            
        m={}
        for x in magazine:
            if x in m:
                m[x]+=1
            else:
                m[x]=1
        
        for x in r:
            if x not in m:
                return False
            if r[x]>m[x]:
                return False
            
        return True
          
        
           
       
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
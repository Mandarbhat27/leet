class Solution(object):
    def simplifyPath(self, path):
        stack=[]

        part=path.split("/")

        for p in part:
            if p=="" or p==".":
                continue
            if p=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return "/"+"/".join(stack)
            
            
        """
        :type path: str
        :rtype: str
        """
        
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        comps = path.split(sep = '/')
        stack = []
         
        for c in comps:
            if not c or c == "." or c == '/':
				# ignore these 
                continue
            elif c == "..":
				# if we can go back a directory
                if stack:
                    stack.pop()
            else:
				# this is a normal directory name, add to stack
                stack.append(c)
        # join what's left in stack with '/' characters
        res = "/".join(c for c in stack)
        return '/' + res
        

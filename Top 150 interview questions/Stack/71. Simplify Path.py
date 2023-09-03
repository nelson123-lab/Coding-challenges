class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        file = ""

        for cF in path + "/":
		
            if cF == "/":
                if file != "" and file != "." and file != "..": # appending to stack
                    stack.append(file)
                elif file == "..": # poping out of the stack if there exist a value in stack.
                    if stack: stack.pop()
                file = "" # Making the value of the file to empty string.
		    
            else: file += cF
        return "/" + "/".join(stack)
        
"""
- Since we need to remove the file of the current storage if the file is "..", we are using a stack to keep track of the job location.
Time Complexity O(n)
- There is one iteration happening here. The time complexity of join operation is O(n) but this is outside the for loop.
Space Complexiy O(n)
- The space used by stack
"""

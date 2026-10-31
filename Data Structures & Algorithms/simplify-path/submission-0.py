class Solution:
    def simplifyPath(self, path: str) -> str:

        s = []

        split = path.split("/")  

        for part in split:

            if part == "" or part == ".":
                continue 

            elif part == ".." :
                if s :
                    s.pop()

            else:
                s.append(part)
        return "/"+"/".join(s)
        
        
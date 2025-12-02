class Solution:
    def simplifyPath(self, path: str) -> str:
        path_splitted = path.split('/')
        path_stack = ['/']

        for c in path_splitted:
            if c == "" or c == ".":
                pass
            elif c == "..":
                if len(path_stack) <= 2:
                    path_stack = ['/']
                else:
                    path_stack.pop()
                    path_stack.pop()
            else:
                path_stack.append(c)
                path_stack.append('/')

        if path_stack[-1] == "/" and len(path_stack) > 1:
            path_stack.pop()

        return "".join(path_stack)
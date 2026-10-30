class Solution:
    def isValid(self, s: str) -> bool:
        open_parenthesis = ['{', '[', '(']
        close_parenthesis = ['}', ']', ')']
        parenthesis = []
        
        for char in s:
            if char in open_parenthesis:
                parenthesis.append(char)
            elif char in close_parenthesis:
                pos = close_parenthesis.index(char)

                if parenthesis and parenthesis[-1] == open_parenthesis[pos]:
                    parenthesis.pop()
                else:
                    return False
        return True if not parenthesis else False        
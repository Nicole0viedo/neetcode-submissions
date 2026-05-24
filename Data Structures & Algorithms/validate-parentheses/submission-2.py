class Solution:
    def isValid(self, s: str) -> bool:
        seen = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                seen.append(c)
            elif  c == ')':
                if len(seen) == 0 or seen.pop() != '(' :
                    return False
            elif  c == '}':
                if len(seen) == 0 or seen.pop() != '{':
                    return False    
            elif  c == ']':
                if len(seen) == 0 or seen.pop() != '[':
                    return False
        if len(seen) == 0:
            return True

        return False
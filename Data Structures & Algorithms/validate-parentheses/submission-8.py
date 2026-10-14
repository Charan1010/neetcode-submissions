class Solution:
    def isValid(self, s: str) -> bool:

        paranthesis_match = { ')' : '(', '}' : '{', ']' : '['}
        paranthesis_stack = []

        for ele in s:
            if ele in paranthesis_match :
                if len(paranthesis_stack) == 0 or paranthesis_match[ele] != paranthesis_stack[-1]:
                    return False
                else:
                    del paranthesis_stack[-1]
                    
            else:
                paranthesis_stack.append(ele)

        #print(paranthesis_stack)

        if len(paranthesis_stack) == 0:
            return True
        else:
            return False


        
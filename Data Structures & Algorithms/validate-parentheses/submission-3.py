class Solution:
    def isValid(self, s: str) -> bool:

        bracket_dict = {')':'(', '}':'{', ']' : '['}

        bracket_stack = []

        for ele in s:

            if ele in bracket_dict:

                last_ele = bracket_stack.pop() if len(bracket_stack) > 0 else None

                if last_ele != bracket_dict[ele]:
                    return False
            else:
                bracket_stack.append(ele)

        if len(bracket_stack) == 0:
            return True
        else:
            return False


        
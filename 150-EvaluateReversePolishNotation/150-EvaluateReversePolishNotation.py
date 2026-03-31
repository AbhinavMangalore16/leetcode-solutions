# Last updated: 3/31/2026, 9:39:27 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        result = 0
        for i in range(len(tokens)):
            stk.append(tokens[i])
            if stk[-1] == "+" or stk[-1] == "-" or stk[-1] == "*" or stk[-1] == "/":
                o = stk.pop()
                n1 = int(stk.pop())
                n2 = int(stk.pop())
                if o == "+":
                    result = (n2+n1)
                elif o == "-":
                    result = (n2-n1)
                elif o == "*":
                    result = (n2*n1)
                elif o == "/":
                    result = (n2/n1)
                stk.append(result)
        if len(stk)==1:
            return int(stk[-1])
        return result          
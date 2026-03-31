# Last updated: 3/31/2026, 9:41:06 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stk = []
        opens = 0
        back = 0
        wellformed = []

        def generate(opens, back, n):
            if opens==back==n:
                wellformed.append("".join(stk))
                return
            if opens<n:
                stk.append("(")
                generate(opens+1, back,n)
                stk.pop()
            if back<opens:
                stk.append(")")
                generate(opens, back+1,n)
                stk.pop()
        generate(opens, back, n)
        return wellformed     
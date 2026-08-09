class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def b(s, open, close):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if open < n:
                b(s + "(", open + 1, close)
            if close < open:
                b(s + ")", open, close + 1)
        b("", 0, 0)
        return ans
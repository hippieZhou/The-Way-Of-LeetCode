class Solution:
    def generateParenthesis(self, n: int) -> list:
        self.ans = []
        self.generate(0, 0, n, '')
        return self.ans

    def generate(self, left: int, right: int, level: int, s: str):
        if left == right == level:
            self.ans.append(s)
            return

        if left < level:
            self.generate(left+1, right, level, s+'(')
        if right < left:
            self.generate(left, right+1, level, s+')')


v = Solution().generateParenthesis(3)
print(v)

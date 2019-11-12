class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = ans[i][j-1] + ans[i-1][j]
        return ans[-1][-1]

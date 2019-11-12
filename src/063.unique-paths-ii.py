class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * (n-1)
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    if j >= 1 and not obstacleGrid[i][j-1]:
                        dp[j] += dp[j-1]
                else:
                    dp[j] = 0
        return dp[-1]

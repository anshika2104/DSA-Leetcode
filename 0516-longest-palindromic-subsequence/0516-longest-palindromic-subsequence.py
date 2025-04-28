class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rs=s[::-1]
        m,n=len(s),len(rs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(0,m):
            for j in range(0,n):
                if s[i]==rs[j]:
                    dp[i+1][j+1]=1+dp[i][j]
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[m][n]

        
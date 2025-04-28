class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # -----------------------------recursion----------------------------
        # def rec(i,j):
        #     if i==len(text1) or j==len(text2):
        #         return 0
        #     if text1[i]==text2[j]:
        #         return (1+rec(i+1,j+1))
        #     else:
        #         return max(rec(i+1,j),rec(i,j+1))
        # return rec(0,0)


        # ----------------------memoization-----------------------------------------------
        # memo={}
        # def rec(i,j):
        #     if i==len(text1) or j==len(text2):
        #         return 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if text1[i]==text2[j]:
        #         return (1+rec(i+1,j+1))
        #     else:
        #         memo[(i,j)]= max(rec(i+1,j),rec(i,j+1))
        #         return memo[(i,j)]
        # return rec(0,0)
        # ---tabulation--------------------
        m,n=len(text1),len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(0,m):
            for j in range(0,n):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=1+dp[i][j]
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[m][n]


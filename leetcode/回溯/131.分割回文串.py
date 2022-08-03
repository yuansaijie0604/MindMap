#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
    #     res = []

    #     def dfs(track, start):
    #         if start>=len(s):
    #             res.append(track[:])
    #         for i in range(start, len(s)):
    #             if self._isPalindrome(s[start:i+1]):
    #                 track.append(s[start:i+1])
    #                 dfs(track, i+1)
    #                 track.pop(-1)

    #     dfs([], 0)

    #     return res

    # def _isPalindrome(self, s: str) -> bool:
    #     i, j = 0, len(s)-1
    #     while i<j:
    #         if s[i]!=s[j]:
    #             return False
    #         i, j = i+1, j-1
    #     return True

        dp = [[True] * len(s) for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                dp[i][j] = (s[i]==s[j] and dp[i+1][j-1])

        res = []
        track = []
        def dfs(start):
            if start == len(s):
                res.append(track[:])
                return

            for i in range(start, len(s)):
                if dp[start][i]:
                    track.append(s[start:i+1])
                    dfs(i+1)
                    track.pop(-1)
        dfs(0)
        return res


# @lc code=end


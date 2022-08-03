#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, sr, sc):
            if sr == 9: return True
            if sc == 9:
                return dfs(board, sr+1, 0)
            if board[sr][sc] != '.':
                return dfs(board, sr, sc+1)
            
            for i in range(1, 10):
                if not is_valid(str(i), sr, sc, board):
                    continue
                board[sr][sc] = str(i)
                if dfs(board, sr, sc+1):
                    return True
                
                board[sr][sc] = '.'

            return False

        def is_valid(n, row, col, track):
            for i in range(9):
                if track[row][i] == n: return False
                if track[i][col] == n: return False
                if track[int(row/3)*3+int(i/3)][int(col/3)*3+i%3] == n: return False
            return True

        dfs(board, 0, 0)

# @lc code=end


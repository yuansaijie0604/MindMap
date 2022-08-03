#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def get_queen(track):
            if len(track) == n:
                res.append(self.draw_chess(track[:]))
            
            for i in range(n):
                if not self.is_valid(track, i):
                    continue
                track.append(i)
                get_queen(track)
                track.pop(-1)
                
        get_queen([])

        return res


    def is_valid(self, track, idx) -> bool:
        if idx in track:
            return False

        len_ = len(track)
        for i, x in enumerate(track):
            if idx in [x-len_+i, x+len_-i]:
                return False

        return True


    def draw_chess(self, track):
        result = []
        len_ = len(track)
        for t in track:
            result.append("."*t + "Q" + "."*(len_-t-1))
        return result

# @lc code=end


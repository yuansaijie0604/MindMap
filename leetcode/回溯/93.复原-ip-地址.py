#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        思路：砍三刀
        """
        res = []

        def dfs(k, s, start, track):
            if k == 0:
                if is_valid(s[start:]):
                    res.append(".".join(track) + "."+ s[start:])
                return
            
            for i in range(start+1, min(start+4, len(s))):
                if not is_valid(s[start:i]):
                    continue
                track.append(s[start:i])
                dfs(k-1, s, i, track)
                track.pop(-1)

        def is_valid(ip):
            if ip[0] == '0' and ip!='0':
                return False
            if int(ip) > 255:
                return False
            return True

        dfs(3, s, 0, [])
        return res

# @lc code=end


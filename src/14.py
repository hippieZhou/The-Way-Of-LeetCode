# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"


class Solution:
    def longestCommonPrefix(self, strs: list) -> int:
        if len(strs) < 1:
            return ""
        else:
            strs = sorted(strs)
            for i, x in enumerate(strs[0]):
                for y in strs[1:]:
                    if x != y[i]:
                        return strs[0][0:i]
            return strs[0]


val = Solution().longestCommonPrefix(["flower", "flow", "flight"])
print(val)

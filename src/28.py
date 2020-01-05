# 实现 strStr() 函数。

# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

        # if needle == None or len(needle) == 0:
        #     return 0
        # length = len(haystack.split(needle)[0])
        # return length if length < len(haystack) else -1


result = Solution().strStr('hello', 'o')
print(result)

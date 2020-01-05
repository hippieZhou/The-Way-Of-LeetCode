# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

# 示例 1:

# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc"


class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = ' '.join(s.split(' ')[::-1])
        print(s1)
        return s1[::-1]


s1 = Solution().reverseWords("Let's take LeetCode contest")
print(s1)

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# 示例 1:

# 输入: 123
# 输出: 321
#  示例 2:

# 输入: -123
# 输出: -321
# 示例 3:

# 输入: 120
# 输出: 21


class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        array = []
        val = abs(x)
        while val > 0 :
            array.append(val % 10)
            val = val // 10
            
        while len(array) > 0:
            v = array.pop(0)
            sum += v * 10 ** len(array)
        return 0 if sum > 2 ** 31 else (sum if x >0 else -sum)

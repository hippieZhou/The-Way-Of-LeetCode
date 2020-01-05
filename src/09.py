# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[-1::-1]
        
        # if x < 0:
        #     return False
        # else:
        #     array = []
        #     while(x > 0):
        #         array.append(x % 10)
        #         x = x // 10
        #     return array == array[-1::-1]


# print(123 / 10)
# print(123 // 10)
# print(123 % 10)

b = Solution().isPalindrome(0)
print(b)

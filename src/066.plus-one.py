class Solution:
    # def plusOne(self, digits: list) -> list:
    #     if len(digits) == 1 and digits[0] == 9:
    #         return [1, 0]

    #     if digits[-1] != 9:
    #         digits[-1] += 1
    #         return digits
    #     else:
    #         digits[-1] = 0
    #         digits[:-1] = self.plusOne(digits[:-1])
    #         return digits

    def plusOne(self, digits: list) -> list:
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)


v = Solution().plusOne([9])
print(v)

class Solution:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     perms = [[]]
    #     for n in nums:
    #         perms = [p[:i] + [n] + p[i:]
    #                  for p in perms
    #                  for i in range((p + [n]).index(n) + 1)]
    #     return perms

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            temp = []
            for item in ans:
                for i in range(len(item) + 1):
                    temp.append(item[:i] + [n] + item[i:])
                    if i < len(item) and item[i] == n:
                        break
            ans = temp
        return ans

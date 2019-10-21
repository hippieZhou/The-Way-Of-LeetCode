class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        for i, v in enumerate(s):
            dic[v] = dic1.get(v, 0) + 1
        dic2 = {}
        for i, v in enumerate(s):
            dic1[v] = dic2.get(v, 0) + 1
        return dic1.values == dic2


v = Solution().isAnagram("anagtam", "nbgbram")
print(v)

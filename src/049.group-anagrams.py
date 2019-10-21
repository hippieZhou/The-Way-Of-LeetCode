class Solution:
    def groupAnagrams(self, strs: list) -> list:
        ans = []
        li = set([''.join(sorted(x)) for x in strs])
        for item in li:
            temp = []
            for i in strs:
                if sorted(i) == sorted(item):
                    temp.append(i)
            ans.append(temp)
        return ans


v = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(v)

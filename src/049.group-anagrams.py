class Solution:
    def groupAnagrams(self, strs: list) -> list:
        hashmap = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in hashmap:
                hashmap[key] += [s]
            else:
                hashmap[key] = [s]
        return hashmap.values()


v = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(v)

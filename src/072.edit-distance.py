class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:
    #     if not word1 and not word2:
    #         return 0
    #     if not word1 or not word2:
    #         return len(word2) or len(word1)

    #     if word1[0] == word2[0]:
    #         return self.minDistance(word1[1:], word2[1:])
    #     insert = 1 + self.minDistance(word1, word2[1:])
    #     delete = 1 + self.minDistance(word1[1:], word2)
    #     replace = 1 + self.minDistance(word1[1:], word2[1:])
    #     return min(insert, replace, delete)

    def minDistance(self, word1: str, word2: str) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            else:
                inserted = helper(i, j + 1)
                deleted = helper(i + 1, j)
                replaced = helper(i + 1, j + 1)
                return min(inserted, deleted, replaced) + 1
        return helper(0, 0)

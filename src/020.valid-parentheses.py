class Solution:
    # def isValid(self, s: str) -> bool:
    #     while '{}' in s or '[]' in s or '()' in s:
    #         s = s.replace('{}', '').replace('[]', '').replace('()', '')
    #     return len(s) == 0

    # def isValid(self, s: str) -> bool:
    #     dic = {'{': '}', '[': ']', '(': ')'}
    #     for c in s:
    #         if c in dic:
    #             stack.append(c)
    #         elif not stack or dic[stack.pop()] != c:
    #             return False
    #     return len(stack) == 0

    def isValid(self, s: str) -> bool:
        dic = {']': '[', '}': '{', ')': '('}
        stack = []
        for c in s:
            if c not in dic:
                stack.append(c)
            elif not stack or stack.pop() != dic[c]:
                return False
        return not stack


v = Solution().isValid(']')
print(v)

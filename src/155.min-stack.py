# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.array = []

#     def push(self, x: int) -> None:
#         self.array.append(x)

#     def pop(self) -> None:
#         self.array.pop()

#     def top(self) -> int:
#         self.array[-1]

#     def getMin(self) -> int:
#         return min(self.array)


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def push(self, x: int) -> None:
        if len(self.array) == 0:
            self.array.append((x, x))
        else:
            self.array.append(x, min(self.getMin(), x))

    def pop(self) -> None:
        self.array.pop()

    def top(self) -> int:
        return self.array[-1][0]

    def getMin(self) -> int:
        return self.array[-1][1] if len(self.array) else None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(12)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

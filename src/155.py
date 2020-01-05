# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。


class MinStack(object):
    def __init__(self):
        self.items = []

    def push(self, x):
        return self.items.append(x)

    def pop(self):
        return self.items.pop()

    def top(self):
        self.items[-1]

    def getMin(self):
        return min(self.items)


stack = MinStack()
print(stack.push(-2))
print(stack.push(0))
print(stack.push(-3))
print(stack.getMin())
print(stack.pop())

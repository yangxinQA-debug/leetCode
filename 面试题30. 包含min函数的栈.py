# -*- coding:utf-8
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_a = []
        self.top_a = -1
        self.stack_b = []
        self.top_b = -1

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.top_a == -1 or x <= self.stack_b[self.top_b]:
            self.stack_b.append(x)
            self.top_b += 1
        self.stack_a.append(x)
        self.top_a += 1

    def pop(self):
        """
        :rtype: None
        """
        if self.top_a == -1:
            return None
        if self.top_b != -1 and self.stack_a[self.top_a] == self.stack_b[self.top_b]:
            self.stack_b.pop(-1)
            self.top_b -= 1
        self.top_a -= 1
        return self.stack_a.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack_a[self.top_a]

    def min(self):
        """
        :rtype: int
        """
        if self.top_b != -1:
            return self.stack_b[self.top_b]
        else:
            return None


if __name__ == "__main__":
    minstack = MinStack()
    minstack.push(0)
    minstack.push(1)
    minstack.push(0)
    print(minstack.min())
    # print(minstack.top())
    print(minstack.pop())
    print(minstack.min())

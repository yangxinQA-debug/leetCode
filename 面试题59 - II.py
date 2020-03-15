# -*-coding:utf-8
"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class MaxQueue(object):

    def __init__(self):
        self.que = []

    def max_value(self):
        """
        :rtype: int
        """
        if len(self.que)==0:
            return -1
        max_value = self.que[0]
        for i in range(len(self.que)):
            if self.que[i] > max_value:
                max_value = self.que[i]
        print(max_value)
        return max_value

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.que.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if len(self.que)==0:
            return -1
        front = self.que[0]
        print(self.que[0])
        self.que = self.que[1:]
        return front

if __name__ =="__main__":
    obj = MaxQueue()
    obj.push_back(1)
    obj.push_back(2)
    param_1 = obj.max_value()
    param_3 = obj.pop_front()
    param_1 = obj.max_value()

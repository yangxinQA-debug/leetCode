# -*- coding:utf-8
"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 复制节点
        p = head
        while p:
            q = Node(p.val)
            q.next = p.next
            p.next = q
            p = q.next
        # 复制random指针：
        p = head
        q = p.next
        while p:
            q = p.next
            if p.random:
                q.random = p.random.next
            if p.random == None:
                q.random = None
            p = q.next
        # 拆分两个链表
        q, head2 = head.next, head.next
        while q.next:
            p.next =q.next
            q.next = q.next.next
            q = q.next
            p = p.next
        return head2


if __name__ == "__main__":
    head = Node(7)
    head.random = None
    head.next = Node(13)
    head.next.random = head
    head.next.next = Node(11)
    head.next.next.next = Node(10)
    head.next.next.next.random = head.next.next
    head.next.next.next.next = Node(1)
    head.next.next.next.next.random = head
    # head.next.random = head.next.next.next.next

    solution = Solution()
    solution.copyRandomList(head)

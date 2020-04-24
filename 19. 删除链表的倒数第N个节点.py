# -*-coding:utf-8
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return head

        p = head
        l = head
        # for i in range(n + 1):
        #     p = p.next
        i = 0
        while i <= n - 1 and p != None:
            p = p.next
            i += 1
        if p == None and i < n - 1:
            return None

        ## 注意删除头结点的情况
        if p == None and i > n - 1:
            return head.next

        while p.next != None:
            p = p.next
            l = l.next
        l.next = l.next.next
        return head


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solution.removeNthFromEnd(head, 2)

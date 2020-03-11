# -*- coding:utf-8
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = None
        node = None
        head = head.next
        while head!=None:
            char = head.val
            head = head.next
            node = ListNode(char)
            node.next = p
            p = node
        list = []
        while (node is not None):
            list.append(node.val)
            node = node.next
        print(list)
        return list

    def buildLink(self, list):
        p = head = ListNode('')
        for i in list:
            q = ListNode(i)
            p.next = q
            p =q
        return head


if __name__ == "__main__":
    input = [1,2,3,4,5]
    solution = Solution()
    head = solution.buildLink(input)
    solution.reverseList(head)

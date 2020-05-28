# -*- coding:utf-8
"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p, q = l1, l2
        if l1 == None and l2 == None:
            return None
        head = ListNode(0)
        r = head
        while p != None and q != None:
            if p.val < q.val:
                r.next = p
                r = r.next
                p = p.next
            elif q.val < p.val:
                r.next = q
                r = r.next
                q = q.next
            else:
                r.next = p
                r = r.next
                p = p.next
                r.next = q
                r = r.next
                q = q.next
        while p != None:
            r.next = p
        while q != None:
            r.next = q
        return head.next

if __name__ =="__main__":
    solution = Solution()
    print(solution.mergeTwoLists(None,None))
# -*- coding:utf-8
"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
"""


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self, pre=None, last=None):
        self.pre = pre
        self.last = last

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        p = root
        while p.left != None:
            p = p.left
        head = p
        self.pre = p
        last = self.inorder(root)
        last.right = head
        head.left = last
        return head

    def inorder(self, root):
        if root.left != None:
            self.inorder(root.left)
        if self.pre != root:
            self.pre.right = root
            root.left = self.pre
            self.pre = root
            self.last = root
        if root.right != None:
            self.inorder(root.right)

        return self.last


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    solutin = Solution()
    solutin.treeToDoublyList(root)

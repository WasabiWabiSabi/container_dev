from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):

    def __init__(self, xs=None):
        super().__init__(xs)

    def balance_factor(self):
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        ret = True
        if node is None:
            return ret
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            ret = False
        if node.left:
            ret &= AVLTree._is_avl_satisfied(node.left)
        if node.right:
            ret &= AVLTree._is_avl_satisfied(node.right)
        return ret

    @staticmethod
    def _left_rotate(node):
        if node is None or node.right is None:
            return node
        new_root = Node(node.right.value)
        new_root.right = node.right.right
        new_root.left = Node(node.value)
        new_root.left.left = node.left
        if node.right.left:
            new_root.left.right = node.right.left
        return new_root

    @staticmethod
    def _right_rotate(node):
        if node is None or node.left is None:
            return node
        new_root = Node(node.left.value)
        new_root.left = node.left.left
        new_root.right = Node(node.value)
        new_root.right.right = node.right
        if node.left.right:
            new_root.right.left = node.left.right
        return new_root

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        if value == self.root.value:
            return
        self.root = AVLTree._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        if value > node.value:
            if node.right:
                AVLTree._insert(node.right, value)
            else:
                node.right = Node(value)
        elif value < node.value:
            if node.left:
                AVLTree._insert(node.left, value)
            else:
                node.left = Node(value)
        if AVLTree._is_avl_satisfied(node):
            pass
        else:
            node.left = AVLTree._rebalance(node.left)
            node.right = AVLTree._rebalance(node.right)
            node = AVLTree._rebalance(node)
        return node

    @staticmethod
    def _rebalance(node):
        bf = AVLTree._balance_factor(node)
        if bf < -1:
            if AVLTree._balance_factor(node.right) > 0:
                new_node = AVLTree._right_rotate(node.right)
                node.right = new_node
                node = AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
            return node
        elif bf > 1:
            if AVLTree._balance_factor(node.left) < 0:
                new_node = AVLTree._left_rotate(node.left)
                node.left = new_node
                node = AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
            return node
        else:
            return node

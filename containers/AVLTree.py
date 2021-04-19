from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):

    def __init__(self, xs=None):
        super().__init__()
        if xs is not None:
            for x in xs:
                self.insert(x)
        self.root = None

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
        if node is None:
            return True
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        left = AVLTree._is_avl_satisfied(node.left)
        right = AVLTree._is_avl_satisfied(node.right)
        return left and right

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
        '''
        FIXME:
        Implement this function.
        '''
        if not self.root:
            self.root = Node(value)
            return
        if value == self.root.value:
            return
        else:
            self._insert(value, self.root)
            if not self.is_avl_satisfied():
                self.root = self.rebalance(self.root)
                if not self.is_avl_satisfied():
                    self.root = self.rebalance(self.root)
            return

    @staticmethod
    def _insert(value, node):
        if node.value == value:
            return
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return
            else:
                return AVLTree._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
                return
            else:
                return AVLTree._insert(value, node.right)
    
    @staticmethod
    def _rebalance(node):
        bf = AVLTree._balance_factor(node)
        if bf < 0:
            if AVLTree._balance_factor(node.right) > 0:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            else:
                AVLTree._left_rotate(node)
        elif bf > 0:
            if AVLTree._balance_factor(node.left) < 0:
                AVLTree._left_rotate(node.left)
                AVLTree._right_rotate(node)
            else:
                AVLTree._right_rotate(node)

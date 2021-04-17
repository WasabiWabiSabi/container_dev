from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):

    def __init__(self, xs=None):
        super().__init__()
        if xs is not None:
            for x in xs:
                self.insert(x)
        self.root = None

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_bst_satisfied(self):
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        if value > node.value:
            if node.right:
                BST._insert(value, node.right)
            else:
                node.right = Node(value)
        if value < node.value:
            if node.left:
                BST._insert(value, node.left)
            else:
                node.left = Node(value)

    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

    def __contains__(self, value):
        return self.find(value)

    def find(self, value):
        if self.root and BST._find(value, self.root):
            return True
        else:
            return False

    @staticmethod
    def _find(value, node):
        if value > node.value and node.right:
            return BST._find(value, node.right)
        if value < node.value and node.left:
            return BST._find(value, node.left)
        if value == node.value:
            return True

    def find_smallest(self):
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        if self.__contains__(value):
            if self.root.value == value and self.height == 1:
                self.root = None
            else:
                self.root = BST._remove(value, self.root)
        else:
            pass

    @staticmethod
    def _remove(value, node):
        if node is None:
            return node
        if value > node.value and node.right:
            node.right = BST._remove(value, node.right)
        if value < node.value and node.left:
            node.left = BST._remove(value, node.left)
        if value == node.value:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                maximum_left = BST._find_largest(node.left)
                node.value = maximum_left
                node.left = BST._remove(maximum_left, node.left)
                return node
        return node

    def remove_list(self, xs):
        for x in xs:
            self.remove(x)

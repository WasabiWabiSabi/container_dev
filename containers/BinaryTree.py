class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left    # NOTE: left should always be a Node
        self.right = right  # NOTE: right should always be a Node

    def __str__(self):
        ret = '('
        ret += str(self.value)
        ret += ' - '
        if self.left:
            ret += str(self.left)
            ret += ' '
        ret += '- '
        if self.right:
            ret += str(self.right)
            ret += ' '
        ret += ')'
        return ret


class BinaryTree():
    def __init__(self, root=None):
        if root:
            self.root = Node(root)
        else:
            self.root = None

    def __str__(self):
        return str(self.root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        else:
            raise ValueError(str(traversal_type) + 'does not work here.')

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + '-'
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal

    def to_list(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder(self.root, [])
        elif traversal_type == 'inorder':
            return self.inorder(self.root, [])
        elif traversal_type == 'postorder':
            return self.postorder(self.root, [])
        else:
            raise ValueError(str(traversal_type) + 'does not work here.')

    def preorder(self, start, traversal):
        if start:
            traversal.append(start.value)
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal.append(start.value)
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal.append(start.value)
        return traversal

    def __len__(self):
        return BinaryTree.__len__helper(self.root)

    @staticmethod
    def __len__helper(node):
        count = 0
        if node is None:
            return count
        else:
            if node.left:
                count += BinaryTree.__len__helper(node.left)
            if node.right:
                count += BinaryTree.__len__helper(node.right)
            if node:
                return count + 1

    def height(self):
        return BinaryTree._height(self.root)

    @staticmethod
    def _height(node):
        lt = -1
        rt = -1
        if node is None:
            return -1
        if node.left:
            lt = BinaryTree._height(node.left)
        if node.right:
            rt = BinaryTree._height(node.right)
        return 1 + max(lt, rt)

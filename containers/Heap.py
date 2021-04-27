from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):

    def __init__(self, xs=None):
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        ret = True
        if node.right and not node.left:
            ret &= False
        if node.right:
            if node.right.value >= node.value:
                ret &= Heap._is_heap_satisfied(node.right)
            else:
                ret = False
        if node.left:
            if node.left.value >= node.value:
                ret &= Heap._is_heap_satisfied(node.left)
            else:
                ret = False
        return ret

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            count = self.__len__()
            binary = "{0:b}".format(count + 1)[1:]
            self.root = Heap._insert(self.root, value, binary)

    @staticmethod
    def _insert(node, value, binary):
        if binary[0] == '0':
            if node.left:
                node.left = Heap._insert(node.left, value, binary[1:])
            else:
                node.left = Node(value)
        if binary[0] == '1':
            if node.right:
                node.right = Heap._insert(node.right, value, binary[1:])
            else:
                node.right = Node(value)
# recursively ascend back up the recursive function swapping each time
        if binary[0] == '0':
            if node.left.value < node.value:
                node.value, node.left.value = node.left.value, node.value
                return node
            else:
                return node
        if binary[0] == '1':
            if node.right.value < node.value:
                node.value, node.right.value = node.right.value, node.value
                return node
            else:
                return node

    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        return self.root.value

    def remove_min(self):
        if self.root is not None:
            count = self.__len__()
            binary = "{0:b}".format(count)[1:]
            if len(binary) > 0:
                print('binary =', binary)
                rm_val, self.root = Heap._remove_br(self.root, binary)
                print('removed value =', rm_val, '   self.root = ', self.root)
                self.root.value = rm_val
                print('HEAP =', self.to_list('inorder'))
                Heap._trickle(self.root)
                print('HEAP after trickle = ', self.to_list('inorder'))
            else:
                self.root = None
                print('root node deleted')

    def _remove_br(node, binary):
        if binary[0] == '0':
            if len(binary) == 1:
                rm_val = node.left.value
                node.left = None
            else:
                rm_val, node.left = Heap._remove_br(node.left, binary[1:])
        if binary[0] == '1':
            if len(binary) == 1:
                rm_val = node.right.value
                node.right = None
            else:
                rm_val, node.right = Heap._remove_br(node.right, binary[1:])
        return rm_val, node

    def _trickle(node):
        if Heap._is_heap_satisfied(node):
            print('heap is satisfied')
            return node
        else:
            if node.left and not node.right:
                node.value, node.left.value = node.left.value, node.value
                node.left = Heap._trickle(node.left)
            elif node.right and not node.left:
                node.value, node.right.value = node.right.value, node.value
                node.right = Heap._trickle(node.right)
            elif node.left.value >= node.right.value:
                node.value, node.right.value = node.right.value, node.value
                node.right = Heap._trickle(node.right)
            elif node.right.value >= node.left.value:
                node.value, node.left.value = node.left.value, node.value
                node.left = Heap._trickle(node.left)
        return node

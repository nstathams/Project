class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value=None):
        if self.root is None:
            self.root = BSTNode(key, value)
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = BSTNode(key, value)
                    current.left.parent = current
                    break
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = BSTNode(key, value)
                    current.right.parent = current
                    break
                current = current.right
            else:
                current.value = value
                break

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, key):
        node = self.search(key)
        if node is None:
            return
        if node.left is None and node.right is None:
            self._replace_in_parent(node, None)
        elif node.right is None:
            self._replace_in_parent(node, node.left)
        elif node.left is None:
            self._replace_in_parent(node, node.right)
        else:
            successor = self._find_min_node(node.right)
            node.key = successor.key
            node.value = successor.value
            self._replace_in_parent(successor, successor.right)

    def _replace_in_parent(self, node, new_child):
        if node.parent is None:
            self.root = new_child
        elif node == node.parent.left:
            node.parent.left = new_child
        else:
            node.parent.right = new_child

        if new_child is not None:
            new_child.parent = node.parent

    def _find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node is not None:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node is not None:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if node is None:
            return True
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return (self._is_balanced(node.left) and
                self._is_balanced(node.right))

    def find_min(self):
        if self.root is None:
            return None
        node = self._find_min_node(self.root)
        return node.key

    def find_max(self):
        if self.root is None:
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key

    def successor(self, key):
        node = self.search(key)
        if node is None:
            return None

        if node.right is not None:
            return self._find_min_node(node.right).key

        current = node
        while (current.parent is not None and
                current == current.parent.right):
            current = current.parent
        return current.parent.key if current.parent else None

    def predecessor(self, key):
        node = self.search(key)
        if node is None:
            return None

        if node.left is not None:
            current = node.left
            while current.right is not None:
                current = current.right
            return current.key

        current = node
        while (current.parent is not None and
                current == current.parent.left):
            current = current.parent
        return current.parent.key if current.parent else None
    

bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)

print(bst.search(10))

print(bst.inorder_traversal())

print(bst.height())


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, node):
        self.root = node

    def append(self, value, root=None):
        if not root:
            root = self.root
        if value <= root.value:
            if root.left:
                self.append(value, root.left)
            else:
                root.left = Node(value)
        else:
            if root.right:
                self.append(value, root.right)
            else:
                root.right = Node(value)

    def pre_order(self, visited=[], queue=[]):
        if not queue and not visited:
            queue.append(self.root)
        if queue:
            s = queue.pop(0)
            if s.left:
                queue.append(s.left)
            if s.right:
                queue.append(s.right)
            if s not in visited:
                visited.append(s)
            self.pre_order(visited, queue)
        return visited

    def post_order(self, visited=[], queue=[]):
        if not queue and not visited:
            queue.append(self.root)
        if queue:
            s = queue.pop(0)
            if s not in visited:
                if s.left:
                    queue.append(s.left)
                    self.post_order(visited, queue)
                if s.right:
                    queue.append(s.right)
                    self.post_order(visited, queue)
                visited.append(s)

        return visited

tree = BinaryTree(Node(10))
tree.append(3)
tree.append(4)
tree.append(6)
tree.append(15)
tree.append(12)
tree.append(11)
tree.append(13)
tree.append(16)
traverse = tree.post_order()
for node in traverse:
    print(node.value)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __int__(self):
        self.val = None


class LinkedList:
    def __init__(self):
        self.node = Node()

    def __init__(self, val):
        self.node = Node(val)

    def insert(self, val):
        ref = self.node
        while ref.next:
            ref = ref.next
        ref.next = Node(val)
        return

    def delete(self, val):
        ref = self.node
        if self.node.val == val:
            self.node = self.node.next
            return
        while ref.next:
            if ref.next.val == val:
                ref.next = ref.next.next
                break
            ref = ref.next
        return

    def print(self):
        ref = self.node
        res = ""
        while ref:
            res += str(ref.val) + " => "
            ref = ref.next
        print(res)
        return


list = LinkedList(5)
list.print()
list.insert(9)
list.insert(10)
list.insert(4)
list.print()
list.delete(10)
list.print()

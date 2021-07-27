class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def insert(self, val):
        ref = self
        while ref.next:
            ref = ref.next
        ref.next = Node(val)
        return self

    def delete(self, val):
        ref = self
        if self.val == val:
            self.val = self.next.val
            self.next = self.next.next
            return self
        while ref.next:
            if val == ref.next.val:
                ref.next = ref.next.next
                break
            ref = ref.next
        return self

    def print(self):
        ref = self
        res = ""
        while ref:
            res += str(ref.val) + " => "
            ref = ref.next
        print(res)


node = Node(5)
node.insert(6)
node.insert(9)
node.insert(7)
node.print()
node.delete(7)
node.print()

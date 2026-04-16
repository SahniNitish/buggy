# buggy_data_structures.py
# Contains intentional bugs for AI code testing

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)  # Bug: pops from front (queue behavior), should be pop()

    def peek(self):
        return self.items[0]  # Bug: should return last element, not first

    def is_empty(self):
        return self.items == []  # Works but fragile; not a bug per se

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)  # Bug: inserts at front

    def dequeue(self):
        return self.items.pop(0)  # Bug: combined with enqueue bug, this is LIFO not FIFO

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = LinkedListNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current = new_node  # Bug: should be current.next = new_node

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                # Bug: doesn't return after deleting, continues iterating (may delete multiple)
            current = current.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BinaryTreeNode(value)
            return
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BinaryTreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:  # Bug: equal values always go right, can cause unbalanced tree
            if node.right is None:
                node.right = BinaryTreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.left, value)  # Bug: should search right subtree

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("Stack pop:", s.pop())  # Expect 3, get 1

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue dequeue:", q.dequeue())  # Expect 1, get 3

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print("LinkedList:", ll.to_list())  # Expect [1,2,3], get [1]

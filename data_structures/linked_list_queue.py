class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self) -> str:
        return f"{self.val}"


class LLQueue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def __iter__(self):
        node: Node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.set_next(self.head)
        self.head = node

    def enqueue(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head is None:
            return None

        node_to_remove = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        node_to_remove.set_next(None)
        return node_to_remove

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


ll_queue = LLQueue()
ll_queue.enqueue(Node("John"))
ll_queue.enqueue(Node("Mary"))
ll_queue.enqueue(Node("Jack"))

ll_queue.dequeue()

print(f"{ll_queue}")

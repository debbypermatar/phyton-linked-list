def add_to_front(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node


def add_to_end(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    current = self.head
    while current.next:
        current = current.next
    current.next = new_node


def remove_front(self):
    if self.head is None:
        return
    self.head = self.head.next


def remove_end(self):
    if self.head is None:
        return
    if self.head.next is None:
        self.head = None
        return
    current = self.head
    while current.next.next:
        current = current.next
    current.next = None


def print_linked_list(self):
    current = self.head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

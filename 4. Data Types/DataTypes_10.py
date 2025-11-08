class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                return

            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        elements.append("None")
        print(" <-> ".join(elements))

    def display_reverse(self):
        if not self.head:
            print("None")
            return

        current = self.head
        while current.next:
            current = current.next
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        elements.append("None")

        print(" <-> ".join(elements))


# Пример использования
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()

dll.prepend(0)
dll.display()

dll.delete(2)
dll.display()

dll.display_reverse()

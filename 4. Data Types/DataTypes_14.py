class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def linked_list(*values):
    if not values:
        return LinkedList()

    linked_list = LinkedList()
    linked_list.head = Node(values[0])
    current = linked_list.head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return linked_list


def print_linked_list(linked_list):
    if not linked_list.head:
        print("None")
        return

    elements = []
    current = linked_list.head
    while current:
        elements.append(str(current.value))
        current = current.next
    elements.append("None")
    print(" -> ".join(elements))


def get_node_and_prev(linked_list, index):
    if index < 0 or not linked_list.head:
        return None, None

    if index == 0:
        return linked_list.head, None

    current = linked_list.head
    prev = None

    for i in range(index):
        if not current.next:
            return None, None
        prev = current
        current = current.next

    return current, prev


def swap_nodes(list_pointer1, index1, list_pointer2, index2):
    list1 = list_pointer1[0]
    list2 = list_pointer2[0]

    node1, prev1 = get_node_and_prev(list1, index1)
    node2, prev2 = get_node_and_prev(list2, index2)

    if node1 is None or node2 is None:
        return False
    if prev1 is None:
        list1.head = node2
    else:
        prev1.next = node2

    if prev2 is None:
        list2.head = node1
    else:
        prev2.next = node1

    next1 = node1.next
    next2 = node2.next
    node1.next = next2
    node2.next = next1

    return True


# Пример использования
list1 = linked_list(1, 2, 3, 4)
list2 = linked_list(5, 6, 7, 8)

result = swap_nodes([list1], 2, [list2], 0)
print(result)  # Output: True

print_linked_list(list1)
# Output: 1 -> 2 -> 5 -> 4 -> None

print_linked_list(list2)
# Output: 3 -> 6 -> 7 -> 8 -> None

list1 = linked_list(1, 2, 3)
list2 = linked_list(4, 5, 6)

result = swap_nodes([list1], 1, [list2], 3)
print(result)  # Output: False

print_linked_list(list1)
# Output: 1 -> 2 -> 3 -> None

print_linked_list(list2)
# Output: 4 -> 5 -> 6 -> None

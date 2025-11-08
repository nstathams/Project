class Heap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        if self.is_empty():
            print("Stack is empty")
        root = self.heap[0]
        last = self.heap.pop()

        if not self.is_empty():
            self.heap[0] = last
            self._heapify_down(0)

        return root

    def _heapify_up(self, index):
        if index == 0:
            return

        parent_index = (index - 1) // 2
        parent_value = self.heap[parent_index]
        current_value = self.heap[index]
        should_swap = (
                (self.max_heap and current_value > parent_value) or
                (not self.max_heap and current_value < parent_value)
        )

        if should_swap:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        largest_or_smallest = index

        if left_index < self.size():
            if (self.max_heap and self.heap[left_index] > self.heap[largest_or_smallest]) or \
                    (not self.max_heap and self.heap[left_index] < self.heap[largest_or_smallest]):
                largest_or_smallest = left_index

        if right_index < self.size():
            if (self.max_heap and self.heap[right_index] > self.heap[largest_or_smallest]) or \
                    (not self.max_heap and self.heap[right_index] < self.heap[largest_or_smallest]):
                largest_or_smallest = right_index

        if largest_or_smallest != index:
            self.heap[index], self.heap[largest_or_smallest] = self.heap[largest_or_smallest], self.heap[index]
            self._heapify_down(largest_or_smallest)


# Пример использования
h = Heap(max_heap=True)

h.insert(10)
h.insert(4)
h.insert(15)
h.insert(20)
h.insert(3)

print("Корень кучи:", h.peek())


while not h.is_empty():
    print("Извлеченный элемент:", h.extract())

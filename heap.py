class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, idx):
        return (idx - 1) // 2

    def left_child(self, idx):
        return (2 * idx) + 1

    def right_child(self, idx):
        return (2 * idx) + 2


class Min_heap(Heap):

    def heapify_up(self, idx):
        while idx > 0:
            parent_idx = self.parent(idx)

            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def del_min(self):

        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        last = self.heap.pop()

        self.heap[0] = last

        self.heapify_down(0)

        return root
    def heapify_down(self, idx):
        size = len(self.heap)

        while True:
            left = self.left_child(idx)
            right = self.right_child(idx)

            smallest = idx

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap < self.heap[smallest]:
                smallest = right

            if smallest != idx:
                self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest]

                idx  = smallest

            else:
                break


class Max_heap(Heap):

    def heapify_up(self, idx):
        while idx > 0:
            parent_idx = self.parent(idx)

            if self.heap[idx] > self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def del_max(self):

        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        last = self.heap.pop()

        self.heap[0] = last

        self.heapify_down(0)

        return root

    def heapify_down(self, idx):
        size = len(self.heap)

        while True:
            left = self.left_child(idx)
            right = self.right_child(idx)

            largest = idx

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != idx:
                self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]

                idx  = largest

            else:
                break




class HeapSelect:
    def __init__(self):
        self.min_heap = []  # Min-heap per k piccoli
        self.max_heap = []  # Max-heap per k grandi

    def insert(self, item):
        # Inserisce l'elemento nei due heap
        self.min_heap.append(item)
        self.max_heap.append(-item)  # Invertiamo il segno per il max-heap
        self._move_up(len(self.min_heap) - 1, self.min_heap)
        self._move_up(len(self.max_heap) - 1, self.max_heap)

    def extract(self):
        # Estrae l'elemento minimo (dal min-heap) e massimo (dal max-heap)
        min_item = self.min_heap[0]
        max_item = -self.max_heap[0]  # Ripristiniamo il segno
        self._swap(0, len(self.min_heap) - 1, self.min_heap)
        self._swap(0, len(self.max_heap) - 1, self.max_heap)
        self.min_heap.pop()
        self.max_heap.pop()
        self._move_down(0, self.min_heap)
        self._move_down(0, self.max_heap)
        return min_item, max_item

    def _move_up(self, index, heap):
        # Sposta l'elemento in alto nell'heap finché non trova la sua posizione corretta.
        while index > 0:
            parent = (index - 1) // 2
            if heap[index] < heap[parent]:
                self._swap(index, parent, heap)
                index = parent
            else:
                break

    def _move_down(self, index, heap):
        # Sposta l'elemento in basso nell'heap finché non trova la sua posizione corretta.
        last_index = len(heap) - 1
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child <= last_index and heap[left_child] < heap[smallest]:
                smallest = left_child

            if right_child <= last_index and heap[right_child] < heap[smallest]:
                smallest = right_child

            if smallest != index:
                self._swap(index, smallest, heap)
                index = smallest
            else:
                break

    def _swap(self, i, j, heap):
        # Scambia due elementi nell'heap.
        heap[i], heap[j] = heap[j], heap[i]

    def heap_select(self, array, k):
        for i in range(k):
            self.insert(array[i])

        for i in range(k, len(array)):
            if array[i] < self.max_heap[0]:
                self.extract()
                self.insert(array[i])

        return self.extract()[0]  # Restituisce il k-esimo minimo

# Esempio di utilizzo:
array = [7, 10, 4, 3, 20, 15]
k = 3
heap_selector = HeapSelect()
kth_min = heap_selector.heap_select(array, k)
print(f"Il {k}-esimo elemento più piccolo è: {kth_min}")

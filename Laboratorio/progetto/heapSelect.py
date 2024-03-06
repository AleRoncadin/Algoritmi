class MinHeap:
    def __init__(self):
        # Inizializzazione dell'array che rappresenta l'heap.
        self.heap = []

    def insert(self, item):
        # Aggiunge l'elemento all'heap e riordina per mantenere le proprietà dell'heap.
        self.heap.append(item)
        self._move_up(len(self.heap) - 1)

    def extract(self):
        # Rimuove e ritorna l'elemento minimo dall'heap.
        if self.heap:
            self._swap(0, len(self.heap) - 1)  # Scambia l'elemento con l'ultimo.
            min_item = self.heap.pop()  # Rimuove l'ultimo elemento, che ora è il minimo.
            self._move_down(0)  # Riordina l'heap.
            return min_item
        raise IndexError("extract from an empty heap")

    def _move_up(self, index):
        # Sposta l'elemento in alto nell'heap finché non trova la sua posizione corretta.
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:  # Se l'elemento è minore del genitore.
                self._swap(index, parent)
                index = parent
            else:
                break

    def _move_down(self, index):
        # Sposta l'elemento in basso nell'heap finché non trova la sua posizione corretta.
        last_index = len(self.heap) - 1
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child <= last_index and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child

            if right_child <= last_index and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        # Scambia due elementi nell'heap.
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def build_heap(self, items):
        # Costruisce un heap da una lista di elementi.
        self.heap = items[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._move_down(i)

    def peek(self):
        # Restituisce l'elemento minimo senza rimuoverlo.
        if self.heap:
            return self.heap[0]
        raise IndexError("peek from an empty heap")

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._move_up(len(self.heap) - 1)

    def extract(self):
        if self.heap:
            self._swap(0, len(self.heap) - 1)
            max_item = self.heap.pop()
            self._move_down(0)
            return max_item
        raise IndexError("extract from an empty heap")

    def _move_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _move_down(self, index):
        last_index = len(self.heap) - 1
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index

            if left_child <= last_index and self.heap[left_child] > self.heap[largest]:
                largest = left_child

            if right_child <= last_index and self.heap[right_child] > self.heap[largest]:
                largest = right_child

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def build_heap(self, items):
        self.heap = items[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._move_down(i)

    def peek(self):
        if self.heap:
            return self.heap[0]
        raise IndexError("peek from an empty heap")

def heap_select(array, k):
    n = len(array)
    if k <= n // 2:
        # Utilizza MinHeap per estrarre k volte
        heap = MinHeap()
        heap.build_heap(array)  # Costruisce il MinHeap con tutti gli elementi
        for i in range(k-1):  # Esegue k-1 estrazioni per rimuovere i (k-1) elementi più piccoli
            heap.extract()
        return heap.extract()  # L'elemento estratto qui sarà il k-esimo più piccolo
    else:
        # Utilizza MaxHeap per mantenere i k elementi più piccoli
        heap = MaxHeap()
        for item in array:
            heap.insert(item)
            if len(heap.heap) > k:  # Se la dimensione del heap supera k, rimuove l'elemento massimo
                heap.extract()
        return heap.peek()  # L'elemento massimo nel MaxHeap dei k elementi più piccoli è il k-esimo elemento più piccolo


a = [int(x) for x in input().split(" ") if x]
k = int(input())
print(heap_select(a,k))

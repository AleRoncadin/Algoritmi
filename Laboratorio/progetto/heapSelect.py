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

# Funzione per eseguire l'algoritmo Heap Select.
def heap_select(array, k):
    # Crea la prima heap H1 con l'array fornito.
    heap_H1 = MinHeap()
    heap_H1.build_heap(array)

    # Crea la seconda heap H2 con il minimo di H1.
    heap_H2 = MinHeap()
    heap_H2.insert((heap_H1.peek(), 0))  # Inserisce una tupla contenente il minimo di H1 e il suo indice.

    # Esegue il processo di selezione del k-esimo elemento più piccolo.
    element, index = None, None
    for _ in range(k):
        element, index = heap_H2.extract()  # Estrae il minimo da H2.
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # Inserisce i successori del nodo estratto da H1 in H2.
        if left_child_index < len(heap_H1.heap):
            heap_H2.insert((heap_H1.heap[left_child_index], left_child_index))  # Correzione: Usa il valore del nodo.
        if right_child_index < len(heap_H1.heap):
            heap_H2.insert((heap_H1.heap[right_child_index], right_child_index))  # Correzione: Usa il valore del nodo.
    
    # Dopo k iterazioni, il valore estratto sarà il k-esimo minimo dell'array originale.
    return element

a = [int(x) for x in input().split(" ") if x]
k = int(input())
print(heap_select(a,k))

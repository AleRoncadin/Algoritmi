class MinHeap:
    def __init__(self):
        self.heap = []

    def length(self):
        return len(self.heap)

    def getMin(self):
        assert len(self.heap) > 0, "Heap is empty"
        return self.heap[0]

    def extract(self):
        assert len(self.heap) > 0, "Heap is empty"
        min_elem = self.heap[0]  # salva l'elemento minimo per restituirlo dopo
        self.heap[0] = self.heap[-1]  # sostituisce la radice con l'ultimo elemento
        self.heap.pop()  # rimuove l'ultimo elemento
        self.heapify(0)  # riordina l'heap
        return min_elem

    def insert(self, x):
        self.heap.append(x)  # aggiunge il nuovo elemento alla fine dell'heap
        self.moveup(len(self.heap) - 1)  # Sposta l'elemento nella posizione corretta

    def buildHeap(self, a):
        self.heap = a[:]  # crea una copia dell'array fornito
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.heapify(i)

    def change(self, i, x):
        assert 0 <= i < len(self.heap), "Index out of bounds"
        old = self.heap[i]
        self.heap[i] = x
        if x < old:
            self.moveup(i)
        else:
            self.heapify(i)

    def heapify(self, i):
        l = 2 * i + 1  # Indice del figlio sinistro
        r = 2 * i + 2  # Indice del figlio destro
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def moveup(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.moveup(parent)

h = MinHeap()
while True:
    line = input()
    tokens = line.split(" ")
    command = tokens[0]
    if command == "exit":
        break
    elif command == "build":
        a = [int(x) for x in tokens[1:]]
        h.buildHeap(a)
    elif command == "length":
        print(h.length())
    elif command == "getmin":
        print(h.getMin())
    elif command == "extract":
        h.extract()
    elif command == "insert":
        x = int(tokens[1])
        h.insert(x)
    elif command == "change":
        i, x = int(tokens[1]), int(tokens[2])
        h.change(i, x)
    else:
        print("Unrecognized command")
    print(*h.heap)

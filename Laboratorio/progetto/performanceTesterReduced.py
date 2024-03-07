import time
import random
from heapSelect import heap_select
from medianOfMedians import median_of_medians
from quickSelect import quickSelect

def resolution():
    start = time.monotonic()
    while time.monotonic() == start:
        pass
    stop = time.monotonic()
    return stop - start

def generate_test_case(n):
    array = [random.randint(0, 1000000) for _ in range(n)]
    k = random.randint(1, n)
    return array, k

def measure_time(algorithm, array, k):
    start = time.monotonic()
    result = algorithm(array, k)
    stop = time.monotonic()
    return stop - start, result

def main():
    R = resolution()
    E = 0.001
    Tmin = R * (1/E + 1)
    
    # Riduci il numero di lunghezze degli array testate per diminuire il tempo totale dei test.
    A = 100  # Mantieni il valore iniziale di A
    B = (5000 / A) ** (1/9)  # Modifica B per avere meno campioni e un massimo di 5000

    algorithms = {
        'Heap Select': heap_select,
        'Median of Medians': median_of_medians,
        'Quick Select': quickSelect
    }

    # Usa solo 10 campioni invece di 100 per accelerare i test.
    for i in range(10):
        n = int(A * B ** i)
        array, k = generate_test_case(n)
        for name, algorithm in algorithms.items():
            # Inizializza il tempo totale e il numero di iterazioni.
            total_time, iterations = 0, 0
            # Genera nuovi casi di test finché il tempo totale non supera Tmin.
            while total_time < Tmin:
                array, k = generate_test_case(n)
                time_spent, _ = measure_time(algorithm, array, k)
                total_time += time_spent
                iterations += 1
            # Calcola il tempo medio di esecuzione.
            avg_time = total_time / iterations
            print(f"Algoritmo: {name}, Lunghezza n: {n}, Tempo medio di esecuzione: {avg_time:.6f} secondi")

if __name__ == "__main__":
    main()

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

# Funzione per generare i casi peggiori
def generate_worst_case_scenario(n, algorithm_name):
    if algorithm_name == 'Median of Medians' or algorithm_name == 'Quick Select':
        # Per questi algoritmi, un caso pessimo può essere un array già ordinato.
        array = list(range(n))
        k = n // 2  # Scegli un k medio per enfatizzare l'effetto.
    else:  # 'Heap Select' o altri algoritmi potrebbero avere casi pessimi diversi.
        # Genera un caso generico che potrebbe essere difficile per heap_select.
        array = [random.randint(0, 1000000) for _ in range(n)]
        array.sort(reverse=True)  # Un array ordinato al contrario può essere un caso pessimo.
        k = 1  # Scegliere il più piccolo elemento potrebbe essere pessimo per l'heap select.
    return array, k

def measure_time(algorithm, array, k):
    start = time.monotonic()
    result = algorithm(array, k)
    stop = time.monotonic()
    return stop - start, result

def main():
    try:
        print("Premi CTRL-C per arrestare il programma")
        R = resolution()
        E = 0.001
        Tmin = R * (1/E + 1)
        
        # Stampa il valore di Tmin per il debug
        print(f"Tmin: {Tmin}")

        A = 100
        B = (5000 / A) ** (1/9)

        algorithms = {
            'Heap Select': heap_select,
            'Median of Medians': median_of_medians,
            'Quick Select': quickSelect
        }

        for i in range(10):
            n = int(A * B ** i)
            # Genera un singolo caso di test per ogni dimensione di n
            array, k = generate_test_case(n)
            for name, algorithm in algorithms.items():
                # Stampa l'algoritmo corrente e la dimensione di n per il debug
                print(f"\nTestando algoritmo: {name} con n = {n}")
                
                total_time, iterations = 0, 0
                # Utilizza lo stesso caso di test per tutte le iterazioni
                while total_time < Tmin:
                    time_spent, _ = measure_time(algorithm, array, k)
                    total_time += time_spent
                    iterations += 1
                
                avg_time = total_time / iterations

                # Stampa i risultati nel caso medio
                print(f"[Caso Medio] Algoritmo: {name}, Lunghezza n: {n}, Tempo medio di esecuzione: {avg_time:.6f} secondi")

                # Stampa i risultati nel caso peggiore
                array, k = generate_worst_case_scenario(n, name)
                time_spent, _ = measure_time(algorithm, array, k)
                print(f"[Caso Pessimo] Algoritmo: {name}, Lunghezza n: {n}, Tempo: {time_spent:.6f} secondi")

    except KeyboardInterrupt:
        print("Chiusura del programma...")

if __name__ == "__main__":
    main()

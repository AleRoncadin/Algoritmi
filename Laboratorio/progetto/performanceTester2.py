import time
import random
from heapSelect import heap_select
from medianOfMedians import median_of_medians
from quickSelect import quickSelect
import matplotlib.pyplot as plt

# Definisce una funzione per calcolare la risoluzione del clock di sistema.
def resolution():
    start = time.monotonic()  # Registra il tempo di inizio.
    while time.monotonic() == start:  # Resta in attesa fino al cambio del tempo registrato per determinare la minima risoluzione temporale.
        pass
    stop = time.monotonic()  # Registra il tempo di fine.
    return stop - start  # Ritorna la differenza, che rappresenta la risoluzione del clock.

# Funzione per generare un caso di test: un array di lunghezza n con valori casuali e un valore k casuale.
def generate_test_case(n):
    array = [random.randint(0, 1000000) for _ in range(n)]  # Genera un array di n numeri casuali tra 0 e 1000000.
    k = random.randint(1, n)  # Seleziona un valore casuale di k nell'intervallo 1 a n.
    return array, k  # Ritorna l'array e il valore di k.

# Funzione per generare i casi peggiori
def generate_worst_case_scenario(n, algorithm_name):
    if algorithm_name == 'Heap Select':
        # Caso peggiore per Heap Select
        array = [random.randint(0, 1000000) for _ in range(n)]
        array.sort(reverse=True)
        k = n // 2
    elif algorithm_name == 'Median of Medians':
        # Caso peggiore per Median of Medians
        array = [i for i in range(n//2) for _ in range(2)]  # Array ordinato con molti duplicati
        k = n // 2
    elif algorithm_name == 'Quick Select':
        # Caso peggiore per Quick Select
        array = list(range(n))
        k = n // 2
    else:
        raise ValueError("Algorithm name not recognized")
    return array, k

# Funzione per misurare il tempo di esecuzione di un algoritmo dato l'array e il valore k.
def measure_time(algorithm, array, k, Tmin):
    total_time, iterations = 0, 0
    while total_time < Tmin:
        start = time.monotonic()  # Tempo di inizio.
        algorithm(array, k)  # Esegue l'algoritmo con l'array e k forniti.
        stop = time.monotonic()  # Tempo di fine.
        time_spent = stop - start
        total_time += time_spent
        iterations += 1
    avg_time = total_time / iterations
    return avg_time

# Funzione per generare i grafici
def generate_graphs(times, algorithms):
    for name in algorithms.keys():
        # Grafico in scala lineare
        plt.figure(figsize=(12, 6))
        if times[name]['avg']:
            n_values_avg = [x[0] for x in times[name]['avg']]
            times_avg = [x[1] for x in times[name]['avg']]
            plt.plot(n_values_avg, times_avg, label='Caso Medio')
        if times[name]['worst']:
            n_values_worst = [x[0] for x in times[name]['worst']]
            times_worst = [x[1] for x in times[name]['worst']]
            plt.plot(n_values_worst, times_worst, label='Caso Pessimo')
        plt.title(f'Prestazioni di {name} (Scala Lineare)')
        plt.xlabel('Lunghezza dell\'array (n)')
        plt.ylabel('Tempo medio di esecuzione (secondi)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'{name}_linear_graph.png')
        plt.close()

        # Grafico in scala log-log
        plt.figure(figsize=(12, 6))
        if times[name]['avg']:
            plt.plot(n_values_avg, times_avg, label='Caso Medio')
        if times[name]['worst']:
            plt.plot(n_values_worst, times_worst, label='Caso Pessimo')
        plt.title(f'Prestazioni di {name} (Scala Log-Log)')
        plt.xlabel('log(Lunghezza dell\'array)')
        plt.ylabel('log(Tempo medio di esecuzione)')
        plt.xscale('log')
        plt.yscale('log')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'{name}_loglog_graph.png')
        plt.close()

# Funzione principale
def main():
    print("Premere CTRL+C in qualsiasi momento per uscire dal programma.")
    R = resolution()
    E = 0.001
    Tmin = R * (1/E + 1)
    A = 100
    B = (100000 / A) ** (1 / 99)
    algorithms = {
        'Heap Select': heap_select,
        'Median of Medians': median_of_medians,
        'Quick Select': quickSelect
    }
    times = {name: {'avg': [], 'worst': []} for name in algorithms.keys()}
    try:
        for i in range(100):
            n = int(A * B ** i)
            array, k = generate_test_case(n)
            for name, algorithm in algorithms.items():
                avg_time = measure_time(algorithm, array, k, Tmin)
                times[name]['avg'].append((n, avg_time))
                print(f"[Caso Medio] Algoritmo: {name}, Lunghezza n: {n}, Tempo medio di esecuzione: {avg_time:.6f} secondi")
                array_worst, k_worst = generate_worst_case_scenario(n, name)
                avg_time_worst = measure_time(algorithm, array_worst, k_worst, Tmin)
                times[name]['worst'].append((n, avg_time_worst))
                print(f"[Caso Pessimo] Algoritmo: {name}, Lunghezza n: {n}, Tempo: {avg_time_worst:.6f} secondi")

    except KeyboardInterrupt:
        print("Uscita dal programma...")
    
    generate_graphs(times, algorithms) # infine vengono generati i grafici

if __name__ == "__main__":
    main()

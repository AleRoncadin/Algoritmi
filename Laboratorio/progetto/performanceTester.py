import time  # Per misurare i tempi di esecuzione.
import random  # Per generare array e valori di k casuali.
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

# Funzione principale che esegue il benchmark degli algoritmi.
def main():
    try:
        print("Premere CTRL+C in qualsiasi momento per uscire dal programma.")

        R = resolution()  # Ottiene la risoluzione del clock.
        E = 0.001  # Imposta l'errore relativo massimo ammissibile.
        Tmin = R * (1/E + 1)  # Calcola il tempo minimo misurabile basato sulla risoluzione e sull'errore relativo.

        # Calcola i valori A e B per generare lunghezze di array in una serie geometrica.
        A = 100
        B = (100000 / A) ** (1/99)

        # Dizionario che mappa i nomi degli algoritmi alle loro funzioni corrispondenti.
        algorithms = {
            'Heap Select': heap_select,
            'Median of Medians': median_of_medians,
            'Quick Select': quickSelect
        }

        # Dizionario per memorizzare i tempi di esecuzione per ogni algoritmo
        times = {name: {'avg': [], 'worst': []} for name in algorithms.keys()}

        # Ciclo per testare gli algoritmi su array di lunghezze variabili.
        for i in range(10):
            n = int(A * B ** i)  # Calcola la lunghezza dell'array per l'attuale iterazione.
            array, k = generate_test_case(n)  # Genera un caso di test.
            
            # Itera attraverso ciascun algoritmo nel dizionario.
            for name, algorithm in algorithms.items():
                avg_time = measure_time(algorithm, array, k, Tmin)
                times[name]['avg'].append(avg_time)
                
                # Stampa i risultati nel caso medio
                print(f"[Caso Medio] Algoritmo: {name}, Lunghezza n: {n}, Tempo medio di esecuzione: {avg_time:.6f} secondi")
                
                array_worst, k_worst = generate_worst_case_scenario(n, name)
                avg_time_worst = measure_time(algorithm, array_worst, k_worst, Tmin)
                times[name]['worst'].append(avg_time_worst)

                # Stampa i risultati nel caso peggiore
                print(f"[Caso Pessimo] Algoritmo: {name}, Lunghezza n: {n}, Tempo: {avg_time_worst:.6f} secondi")
    
        # Crea i grafici
        for name in algorithms.keys():
            plt.figure(figsize=(10, 5))
            plt.plot(times[name]['avg'], label='Caso Medio')
            plt.plot(times[name]['worst'], label='Caso Pessimo')
            plt.title(name)
            plt.xlabel('Iterazione')
            plt.ylabel('Tempo medio di esecuzione (secondi)')
            plt.legend()
            plt.savefig(f'{name}_graph.png') # Salva il grafico in un file

    except KeyboardInterrupt:
        print("Uscita dal programma...")

if __name__ == "__main__":
    main()

import time  # Per misurare i tempi di esecuzione.
import random  # Per generare array e valori di k casuali.
from heapSelect import heap_select
from medianOfMedians import median_of_medians
from quickSelect import quickSelect

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

# Funzione per misurare il tempo di esecuzione di un algoritmo dato l'array e il valore k.
def measure_time(algorithm, array, k):
    start = time.monotonic()  # Tempo di inizio.
    result = algorithm(array, k)  # Esegue l'algoritmo con l'array e k forniti.
    stop = time.monotonic()  # Tempo di fine.
    return stop - start, result  # Ritorna il tempo trascorso e il risultato dell'algoritmo.

# Funzione principale che esegue il benchmark degli algoritmi.
def main():
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

    # Ciclo per testare gli algoritmi su array di lunghezze variabili.
    for i in range(100):
        n = int(A * B ** i)  # Calcola la lunghezza dell'array per l'attuale iterazione.
        array, k = generate_test_case(n)  # Genera un caso di test.
        # Itera attraverso ciascun algoritmo nel dizionario.
        for name, algorithm in algorithms.items():
            total_time, iterations = 0, 0  # Inizializza il tempo totale e il conteggio delle iterazioni.
            # Continua ad eseguire l'algoritmo su nuovi casi di test finché il tempo totale è minore di Tmin.
            while total_time < Tmin:
                #array, k = generate_test_case(n)  # Genera un nuovo caso di test.
                time_spent, _ = measure_time(algorithm, array, k)  # Misura il tempo di esecuzione.
                total_time += time_spent  # Aggiorna il tempo totale.
                iterations += 1  # Incrementa il conteggio delle iterazioni.
            avg_time = total_time / iterations  # Calcola il tempo medio di esecuzione.
            
            # Stampa i risultati nel caso medio
            print(f"[Caso Medio] Algoritmo: {name}, Lunghezza n: {n}, Tempo medio di esecuzione: {avg_time:.6f} secondi")

            # Stampa i risultati nel caso peggiore
            array, k = generate_worst_case_scenario(n, name)
            time_spent, _ = measure_time(algorithm, array, k)
            print(f"[Caso Pessimo] Algoritmo: {name}, Lunghezza n: {n}, Tempo: {time_spent:.6f} secondi")

# Verifica se lo script è il punto di ingresso principale e, in tal caso, esegue la funzione main().
if __name__ == "__main__":
    main()

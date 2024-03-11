import time

def resolution():
    start = time.monotonic()
    while time.monotonic() == start:
        pass
    stop = time.monotonic()
    return stop - start

def main():
    print("Eseguo il main")
    R = resolution()
    E = 0.001
    Tmin = R * (1/E + 1)
    # Stampa il valore di Tmin per il debug
    print(f"Tmin: {Tmin}")

if __name__ == "__main__":
    main()

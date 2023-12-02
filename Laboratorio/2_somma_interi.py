from __future__ import print_function

try: input = raw_input
except NameError: pass

# Leggi due interi separati da uno spazio
input_string = input()
x, y = map(int, input_string.split())

# Calcola la somma
somma = x + y

# Stampa il risultato
print(somma)
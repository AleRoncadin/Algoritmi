def periodoFrazionario(s):
    n = len(s)
    for p in range(1, n + 1):
        # p è un possibile periodo frazionario, ma devo controllare
        corretto = True
        for i in range(0, n):
            if s[i] != s[i % p]:
                corretto = False
        if corretto:
            return p

s = input()
print(periodoFrazionario(s))     
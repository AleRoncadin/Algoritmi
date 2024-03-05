class NodoAVL:
    def __init__(self, chiave, valore):
        self.chiave = chiave
        self.valore = valore
        self.altezza = 1
        self.sinistro = None
        self.destro = None

    def __str__(self):
        return f"{self.chiave}:{self.valore}:{self.altezza}"


class AlberoAVL:
    def __init__(self):
        self.radice = None

    def getAltezza(self, nodo):
        if not nodo:
            return 0
        return nodo.altezza

    def getBilanciamento(self, nodo):
        if not nodo:
            return 0
        return self.getAltezza(nodo.sinistro) - self.getAltezza(nodo.destro)

    def rotazioneDestra(self, y):
        x = y.sinistro
        T2 = x.destro
        x.destro = y
        y.sinistro = T2
        y.altezza = 1 + max(self.getAltezza(y.sinistro), self.getAltezza(y.destro))
        x.altezza = 1 + max(self.getAltezza(x.sinistro), self.getAltezza(x.destro))
        return x

    def rotazioneSinistra(self, x):
        y = x.destro
        T2 = y.sinistro
        y.sinistro = x
        x.destro = T2
        x.altezza = 1 + max(self.getAltezza(x.sinistro), self.getAltezza(x.destro))
        y.altezza = 1 + max(self.getAltezza(y.sinistro), self.getAltezza(y.destro))
        return y

    def inserisci(self, nodo, chiave, valore):
        if not nodo:
            return NodoAVL(chiave, valore)
        elif chiave < nodo.chiave:
            nodo.sinistro = self.inserisci(nodo.sinistro, chiave, valore)
        else:
            nodo.destro = self.inserisci(nodo.destro, chiave, valore)

        nodo.altezza = 1 + max(
            self.getAltezza(nodo.sinistro), self.getAltezza(nodo.destro)
        )

        bilanciamento = self.getBilanciamento(nodo)

        if bilanciamento > 1 and chiave < nodo.sinistro.chiave:
            return self.rotazioneDestra(nodo)
        if bilanciamento < -1 and chiave > nodo.destro.chiave:
            return self.rotazioneSinistra(nodo)
        if bilanciamento > 1 and chiave > nodo.sinistro.chiave:
            nodo.sinistro = self.rotazioneSinistra(nodo.sinistro)
            return self.rotazioneDestra(nodo)
        if bilanciamento < -1 and chiave < nodo.destro.chiave:
            nodo.destro = self.rotazioneDestra(nodo.destro)
            return self.rotazioneSinistra(nodo)

        return nodo

    def trovaMinNodo(self, nodo):
        while nodo.sinistro is not None:
            nodo = nodo.sinistro
        return nodo

    def rimuovi(self, nodo, chiave):
        if not nodo:
            return nodo

        if chiave < nodo.chiave:
            nodo.sinistro = self.rimuovi(nodo.sinistro, chiave)
        elif chiave > nodo.chiave:
            nodo.destro = self.rimuovi(nodo.destro, chiave)
        else:
            if nodo.sinistro is None:
                temp = nodo.destro
                nodo = None
                return temp
            elif nodo.destro is None:
                temp = nodo.sinistro
                nodo = None
                return temp

            temp = self.trovaMinNodo(nodo.destro)
            nodo.chiave = temp.chiave
            nodo.valore = temp.valore
            nodo.destro = self.rimuovi(nodo.destro, temp.chiave)

        if nodo is None:
            return nodo

        nodo.altezza = 1 + max(
            self.getAltezza(nodo.sinistro), self.getAltezza(nodo.destro)
        )

        bilanciamento = self.getBilanciamento(nodo)

        if bilanciamento > 1 and self.getBilanciamento(nodo.sinistro) >= 0:
            return self.rotazioneDestra(nodo)
        if bilanciamento > 1 and self.getBilanciamento(nodo.sinistro) < 0:
            nodo.sinistro = self.rotazioneSinistra(nodo.sinistro)
            return self.rotazioneDestra(nodo)
        if bilanciamento < -1 and self.getBilanciamento(nodo.destro) <= 0:
            return self.rotazioneSinistra(nodo)
        if bilanciamento < -1 and self.getBilanciamento(nodo.destro) > 0:
            nodo.destro = self.rotazioneDestra(nodo.destro)
            return self.rotazioneSinistra(nodo)

        return nodo

    def preordine(self, nodo):
        if not nodo:
            return "NULL"
        sinistro = self.preordine(nodo.sinistro) if nodo.sinistro else "NULL"
        destro = self.preordine(nodo.destro) if nodo.destro else "NULL"
        return f"{nodo.chiave}:{nodo.valore}:{nodo.altezza} {sinistro} {destro}"

    def ricerca(self, nodo, chiave):
        if nodo is None or nodo.chiave == chiave:
            return nodo
        if chiave < nodo.chiave:
            return self.ricerca(nodo.sinistro, chiave)
        return self.ricerca(nodo.destro, chiave)

    def clear(self):
        self.radice = None


def gestisciComando(albero, comando):
    parti = comando.split()
    operazione = parti[0].lower()
    if operazione == "insert" and len(parti) == 3:
        albero.radice = albero.inserisci(albero.radice, int(parti[1]), parti[2])
    elif operazione == "remove" and len(parti) == 2:
        albero.radice = albero.rimuovi(albero.radice, int(parti[1]))
    elif operazione == "find" and len(parti) == 2:
        risultato = albero.ricerca(albero.radice, int(parti[1]))
        if risultato:
            print(risultato.valore)
        else:
            print("Chiave non trovata.")
    elif operazione == "clear":
        albero.clear()
    elif operazione == "show":
        print(albero.preordine(albero.radice).strip())
    else:
        print("Operazione non supportata.")
        return False
    return True


if __name__ == "__main__":
    albero = AlberoAVL()
    while True:
        comando = input()
        if comando.lower() == "exit":
            break
        if not gestisciComando(albero, comando):
            break

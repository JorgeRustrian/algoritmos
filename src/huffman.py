import heapq

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


def calcular_frecuencias(ruta_txt):
    try:
        with open(ruta_txt, "r", encoding="utf-8") as f:
            texto = f.read()

        frecuencias = {}
        for c in texto:
            frecuencias[c] = frecuencias.get(c, 0) + 1

        return frecuencias

    except FileNotFoundError:
        return None


def construir_arbol_huffman(frecuencias):
    heap = []

    for c, f in frecuencias.items():
        heapq.heappush(heap, NodoHuffman(c, f))

    if len(heap) == 1:
        nodo = heapq.heappop(heap)
        raiz = NodoHuffman(None, nodo.frecuencia)
        raiz.izq = nodo
        return raiz

    while len(heap) > 1:
        izq = heapq.heappop(heap)
        der = heapq.heappop(heap)

        nuevo = NodoHuffman(None, izq.frecuencia + der.frecuencia)
        nuevo.izq = izq
        nuevo.der = der

        heapq.heappush(heap, nuevo)

    return heapq.heappop(heap)


def generar_codigos(raiz):
    codigos = {}

    def recorrer(nodo, codigo_actual):
        if nodo is None:
            return

        if nodo.caracter is not None:
            codigos[nodo.caracter] = codigo_actual
            return

        recorrer(nodo.izq, codigo_actual + "0")
        recorrer(nodo.der, codigo_actual + "1")

    recorrer(raiz, "")
    return codigos


def representacion_textual(raiz, nivel=0):
    if raiz is None:
        return ""

    texto = ""
    texto += representacion_textual(raiz.der, nivel + 1)

    texto += "    " * nivel
    if raiz.caracter is None:
        texto += f"[*] ({raiz.frecuencia})\n"
    else:
        if raiz.caracter == " ":
            texto += f"[espacio] ({raiz.frecuencia})\n"
        else:
            texto += f"[{raiz.caracter}] ({raiz.frecuencia})\n"

    texto += representacion_textual(raiz.izq, nivel + 1)

    return texto

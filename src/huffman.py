import heapq
from graphviz import Digraph
import os

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








def generar_png_huffman(raiz, nombre_archivo="huffman_tree.png"):

    carpeta_output = "./docs/evidencias"
   

    g = Digraph(format="png")
    g.attr("node", shape="circle")

    def agregar_nodos(nodo, nombre):
        """Agrega nodos y conexiones recursivamente."""
        if nodo is None:
            return

        if nodo.caracter is None:
            etiqueta = f"*\\n{nodo.frecuencia}"
        else:
            if nodo.caracter == " ":
                etiqueta = f"espacio\\n{nodo.frecuencia}"
            else:
                etiqueta = f"{nodo.caracter}\\n{nodo.frecuencia}"

        g.node(nombre, etiqueta)

       
        if nodo.izq:
            g.edge(nombre, nombre + "0")
            agregar_nodos(nodo.izq, nombre + "0")

      
        if nodo.der:
            g.edge(nombre, nombre + "1")
            agregar_nodos(nodo.der, nombre + "1")

    agregar_nodos(raiz, "R")

    ruta_png = os.path.join(carpeta_output, nombre_archivo)
    g.render(filename=ruta_png, cleanup=True)

    print(f">> Árbol Huffman PNG generado: {ruta_png}")




def generar_png_frecuencias(frecuencias, nombre_archivo="frecuencias.png"):

    carpeta_output = "./docs/evidencias"
   

    g = Digraph(format="png")
    g.attr(rankdir="LR")  # barras de izquierda a derecha
    g.attr("node", shape="box", height="0.5")

    for c, f in frecuencias.items():
        if c == " ":
            etiqueta = f"espacio ({f})"
        else:
            etiqueta = f"{c} ({f})"

        ancho = str(f * 0.3)  # escala para barras
        g.node(etiqueta, label=etiqueta, width=ancho, style="filled", fillcolor="lightblue")

    ruta_png = os.path.join(carpeta_output, nombre_archivo)
    g.render(filename=ruta_png, cleanup=True)

    print(f">> Frecuencias PNG generado: {ruta_png}")

from graphviz import Graph
import os

def encontrar(padre, nodo):
    
    if padre[nodo] != nodo:
        padre[nodo] = encontrar(padre, padre[nodo])
    return padre[nodo]


def unir(padre, rango, u, v):
    
    raiz_u = encontrar(padre, u)
    raiz_v = encontrar(padre, v)

    if raiz_u != raiz_v:
        if rango[raiz_u] < rango[raiz_v]:
            padre[raiz_u] = raiz_v
        elif rango[raiz_u] > rango[raiz_v]:
            padre[raiz_v] = raiz_u
        else:
            padre[raiz_v] = raiz_u
            rango[raiz_u] += 1


def kruskal(grafo):
   

    if not grafo:
        return None, "El grafo está vacío o no se pudo cargar."

    aristas = []
    for u in grafo:
        for v, peso in grafo[u].items():
          
            if (v, u, peso) not in aristas:
                aristas.append((u, v, peso))

  
    aristas.sort(key=lambda x: x[2])

  
    padre = {nodo: nodo for nodo in grafo}
    rango = {nodo: 0 for nodo in grafo}

    mst = []
    costo_total = 0

  
    for u, v, peso in aristas:
        if encontrar(padre, u) != encontrar(padre, v):
            unir(padre, rango, u, v)
            mst.append((u, v, peso))
            costo_total += peso

 
    if len(mst) != len(grafo) - 1:
        return None, "El grafo no es conexo. No se puede construir un MST completo."

    return mst, costo_total




def generar_png_kruskal(aristas_mst, nombre_archivo="kruskal_mst.png"):
   

  
    carpeta_output = "./docs/evidencias"
    

   
    g = Graph(format="png")

 
    for u, v, peso in aristas_mst:
        g.edge(u, v, label=str(peso))

 
    ruta_png = os.path.join(carpeta_output, nombre_archivo)
    g.render(filename=ruta_png, cleanup=True)

    print("Imagen generada: {ruta_png}")
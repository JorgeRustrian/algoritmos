

from src.cargarDatosCsv import cargar_grafo_csv
from src.prim import prim, generar_png_prim
from src.kruskal import kruskal, generar_png_kruskal
from src.dijkstra import dijkstra, reconstruir_camino, generar_png_dijkstra
from src.huffman import (
    calcular_frecuencias,
    construir_arbol_huffman,
    generar_codigos,
    representacion_textual
)



def mostrar_menu():
    print("0. Salir")
    print("1. Ejecutar Prim")
    print("2. Ejecutar Kruskal")
    print("3. Ejecutar Dijkstra")
    print("4. Ejecutar Huffman")
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo...")
            break

        elif opcion == "1":
            grafo = cargar_grafo_csv("./data/grafos/grafos.csv")  
            print("GRAFO CARGADO:", grafo)

           

            aristas, costo = prim(grafo)

           
            print("\nMST con Prim:")
            for u, v, w in aristas:
                print(f"{u} -- {v}  (peso={w})")

            print("\nCosto total:", costo)
            generar_png_prim(aristas, "prim_mst.png")
        elif opcion == "2":
         grafo = cargar_grafo_csv("./data/grafos/grafos.csv")
         aristas, resultado = kruskal(grafo)

         if aristas is None:
          print("Error:", resultado)
         else:
           print("\nMST con Kruskal:")
           for u, v, w in aristas:
            print(f"{u} -- {v}  (peso={w})")
         print("\nCosto total:", resultado)
         generar_png_kruskal(aristas, "kruskal_mst.png")
       
        elif opcion == "3":  
             grafo = cargar_grafo_csv("./data/grafos/grafos.csv")
             origen = input("Ingrese nodo origen: ")
             resultado, padres = dijkstra(grafo, origen)

             if resultado is None:
               print("Error:", padres)
             else:
              print("\nDistancias más cortas desde", origen)
              for nodo, dist in resultado.items():
               print(f"{origen} -> {nodo}: {dist}")

             destino = input("\n¿Desea reconstruir el camino hacia qué nodo?: ")
             if destino in resultado:
              camino = reconstruir_camino(padres, destino)
              print("\nCamino más corto:", " -> ".join(camino))
              print("Costo:", resultado[destino])
             else:
              print("Nodo destino no existe.")
             generar_png_dijkstra(grafo, camino, "dijkstra_paths.png")
        elif opcion == "4":  
             ruta = "./data/textos/huffman.txt"   
             frecuencias = calcular_frecuencias(ruta)

             if frecuencias is None:
               print("No se pudo leer el archivo.")
             else:
               print("\nFrecuencias:")
               for c, f in frecuencias.items():
                  if c == " ":
                    print(f"[espacio]: {f}")
                  else:
                   print(f"{c}: {f}")

               raiz = construir_arbol_huffman(frecuencias)
               codigos = generar_codigos(raiz)

               print("\nCódigos Huffman:")
               for c, code in codigos.items():
                 if c == " ":
                  print(f"[espacio] = {code}")
                 else:
                   print(f"{c} = {code}")

               print("\nÁrbol (representación textual):")
               print(representacion_textual(raiz))

if __name__ == "__main__":
    main()


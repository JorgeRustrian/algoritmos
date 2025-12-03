def cargar_grafo_csv(ruta_csv):
    grafo = {}

    try:
        with open(ruta_csv, "r") as archivo:
            lineas = archivo.readlines()

            
            encabezado = lineas[0].strip().split(",")

            
            if encabezado != ["origen", "destino", "peso"]:
                raise ValueError("El archivo CSV debe tener columnas: origen,destino,peso")

           
            for linea in lineas[1:]:
                linea = linea.strip()
                if linea == "":
                    continue  

                origen, destino, peso = linea.split(",")

                peso = float(peso)  

              
                if origen not in grafo:
                    grafo[origen] = {}

                if destino not in grafo:
                    grafo[destino] = {}

                grafo[origen][destino] = peso
                grafo[destino][origen] = peso

        return grafo

    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{ruta_csv}'.")
        return None

    except Exception as e:
        print("ERROR al cargar el CSV:", e)
        return None




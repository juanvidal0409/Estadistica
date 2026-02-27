import qrcode  # Librería para generar códigos QR
import os      # Librería para manejar rutas y carpetas del sistema

# Carpeta donde se guardarán los QR (misma ubicación del script)
CARPETA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_estadistica")

# Diccionario que contiene los recursos disponibles
# Cada recurso tiene: nombre, URL, descripción y nombre del archivo QR
RECURSOS = {
    1: {
        "nombre": "Khan Academy - Estadistica y Probabilidad",
        "url": "https://es.khanacademy.org/math/statistics-probability",
        "descripcion": "Curso gratuito de estadistica desde cero, en espanol.",
        "archivo": "qr_khanacademy.png",
    },
    2: {
        "nombre": "StatQuest with Josh Starmer (YouTube)",
        "url": "https://www.youtube.com/@statquest",
        "descripcion": "Explicaciones visuales y claras de estadistica y ML.",
        "archivo": "qr_statquest.png",
    },
    3: {
        "nombre": "Seeing Theory - Estadistica Visual",
        "url": "https://seeing-theory.brown.edu",
        "descripcion": "Visualizaciones interactivas de conceptos estadisticos. (Brown University)",
        "archivo": "qr_seeing_theory.png",
    },
    4: {
        "nombre": "Statistics How To",
        "url": "https://www.statisticshowto.com",
        "descripcion": "Enciclopedia de estadistica con ejemplos paso a paso.",
        "archivo": "qr_statistics_howto.png",
    },
    5: {
        "nombre": "Gapminder - Datos Mundiales",
        "url": "https://www.gapminder.org/tools/",
        "descripcion": "Herramienta interactiva para explorar estadisticas globales.",
        "archivo": "qr_gapminder.png",
    },
}


# Función que muestra el menú en consola
def mostrar_menu():
    print("\n" + "=" * 55)
    print("   Generador de QR - Recursos de Estadistica")
    print("=" * 55)
    
    # Recorre el diccionario de recursos y los imprime
    for num, recurso in RECURSOS.items():
        print(f"\n  [{num}] {recurso['nombre']}")
        print(f"       {recurso['descripcion']}")
    
    # Opción para generar todos los QR
    print("\n  [0] Generar TODOS los codigos QR")
    print("=" * 55)


# Función que genera el código QR de un recurso específico
def generar_qr(recurso: dict) -> str:
    
    # Crea la carpeta si no existe
    os.makedirs(CARPETA, exist_ok=True)

    # Configuración del objeto QR
    qr = qrcode.QRCode(
        version=2,  # Controla el tamaño del QR
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nivel alto de corrección de errores
        box_size=10,  # Tamaño de cada cuadro del QR
        border=4,  # Grosor del borde
    )

    # Agrega la URL del recurso al QR
    qr.add_data(recurso["url"])
    qr.make(fit=True)  # Ajusta automáticamente el tamaño

    # Genera la imagen con colores personalizados
    img = qr.make_image(
        fill_color="#1a1a2e",   # Color del QR
        back_color="#f0f4f8",   # Color de fondo
    )

    # Construye la ruta completa donde se guardará el archivo
    ruta = os.path.join(CARPETA, recurso["archivo"])
    
    # Guarda la imagen
    img.save(ruta)
    
    # Retorna la ruta del archivo generado
    return ruta


# Función principal del programa
def main():
    
    # Muestra el menú
    mostrar_menu()

    try:
        # Solicita al usuario una opción
        opcion = int(input("\n  Elige una opcion: "))
    except ValueError:
        # Manejo de error si el usuario no ingresa un número
        print("  Opcion invalida.")
        return

    # Si el usuario elige 0, genera todos los QR
    if opcion == 0:
        print("\n  Generando todos los codigos QR...\n")
        for recurso in RECURSOS.values():
            ruta = generar_qr(recurso)
            print(f"  OK  {recurso['nombre']}")
            print(f"      URL    : {recurso['url']}")
            print(f"      Archivo: {ruta}\n")
        print("  Todos los QR generados.")
        print(f"  Carpeta: {CARPETA}")

    # Si elige una opción válida dentro del diccionario
    elif opcion in RECURSOS:
        recurso = RECURSOS[opcion]
        print(f"\n  Generando QR para: {recurso['nombre']}...")
        ruta = generar_qr(recurso)
        print(f"\n  Codigo QR creado!")
        print(f"      URL    : {recurso['url']}")
        print(f"      Archivo: {ruta}")

    # Si la opción no existe
    else:
        print("  Opcion fuera de rango.")


# Punto de entrada del programa
# Solo ejecuta main() si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
    "link repositorio : https://github.com/juanvidal0409/Estadistica"


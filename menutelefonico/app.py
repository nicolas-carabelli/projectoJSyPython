# Importación de módulos necesarios
import colorama
from colorama import Fore, Style
import random

colorama.init()

# Saldo inicial
SALDO = 1200

# Lista de fragmentos de canciones
FRAGMENTOS = [
    f"{Fore.MAGENTA}Vintage tee, brand new phone. High heels on cobblestones - (Willow){Style.RESET_ALL}",
    f"{Fore.MAGENTA}And when I felt like I was an old cardigan. Under someone's bed - (Cardigan){Style.RESET_ALL}",
    f"{Fore.MAGENTA}And I was thinking on the drive down. 'Anytime now, he's gonna say it's love' - (Champagne Problems){Style.RESET_ALL}",
    f"{Fore.MAGENTA}Time, curious time. Gave me no compasses, gave me no signs - (Evermore) {Style.RESET_ALL}",
    f"{Fore.MAGENTA}All's well that ends well to end up with you. Swore off love until I met you - (Dorothea){Style.RESET_ALL}",
    f"{Fore.MAGENTA}I'm on my tallest tiptoes, spinning in my highest heels / Love, shining just for you - (Long Story Short){Style.RESET_ALL}",
]

# Función para consultar el saldo
def consultar_saldo():
    """
    Función que devuelve el saldo actual.
    """
    return f"{Fore.CYAN}Su saldo actual es de {SALDO}{Style.RESET_ALL}"

# Función para cargar saldo
def cargar_saldo():
    """
    Función que permite al usuario cargar saldo.
    """
    monto = int(input(f"{Fore.YELLOW}Ingrese la cantidad a cargar: {Style.RESET_ALL}"))
    global SALDO
    SALDO += monto
    return f"{Fore.GREEN}Se ha cargado {monto} correctamente. Su saldo actual es de {SALDO}{Style.RESET_ALL}"

# Función para transferir saldo
def transferir_saldo():
    """
    Función que permite al usuario transferir saldo a otra cuenta.
    """
    monto = int(input(f"{Fore.YELLOW}Ingrese la cantidad a transferir: {Style.RESET_ALL}"))
    global SALDO
    if monto <= SALDO:
        SALDO -= monto
        return f"{Fore.GREEN}Se ha transferido {monto} correctamente. Su saldo actual es de {SALDO}{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}Saldo insuficiente para realizar la transferencia{Style.RESET_ALL}"

# Función para obtener un fragmento de la canción "Evermore"
def fragmentos_letras_evermore():
    """
    Función que devuelve un fragmento aleatorio de la canción "Evermore".
    """
    return random.choice(FRAGMENTOS)

# Función para mostrar el menú de opciones
def mostrar_menu():
    """
    Función que muestra las opciones disponibles para el usuario.
    """
    print(f"{Fore.BLUE}Hola!{Style.RESET_ALL}")
    print(f"{Fore.BLUE}1. Consultar Saldo{Style.RESET_ALL}")
    print(f"{Fore.BLUE}2. Cargar Saldo{Style.RESET_ALL}")
    print(f"{Fore.BLUE}3. Transferir Saldo{Style.RESET_ALL}")
    print(f"{Fore.BLUE}4. Para Ti{Style.RESET_ALL}")

# Bucle principal para interactuar con el usuario
while True:
    mostrar_menu()
    opcion = input(f"{Fore.BLUE}Seleccione una opción: {Style.RESET_ALL}")

    if opcion == "1":
        print(consultar_saldo())
    elif opcion == "2":
        print(cargar_saldo())
    elif opcion == "3":
        print(transferir_saldo())
    elif opcion == "4":
        fragmento = fragmentos_letras_evermore()
        print(fragmento)
    else:
        print(f"{Fore.RED}Opción inválida. Por favor, seleccione una opción válida.{Style.RESET_ALL}")

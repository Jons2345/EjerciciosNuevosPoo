import os

# COLORES para la consola
colores = {
    'ROJO': '\033[91m',
    'VERDE': '\033[92m',
    'AZUL': '\033[94m',
    'AMARILLO': '\033[93m',
    'CYAN': '\033[96m',
    'BLANCO': '\033[97m',
    'RESET': '\033[0m'
}

def limpiar_pantalla():
    # Limpia la consola
    os.system('clear' if os.name == 'posix' else 'cls')

def imprimir_color(texto, color):
    # Imprime texto con color
    codigo = colores.get(color, colores['BLANCO'])
    reset = colores['RESET']
    print(f"{codigo}{texto}{reset}")

def imprimir_titulo(texto):
    # Imprime un título bonito
    limpiar_pantalla()
    imprimir_color('='*60, 'AZUL')
    print(f"  {texto}".center(60))
    imprimir_color('='*60, 'AZUL')
    print()

def imprimir_exito(mensaje):
    # Mensaje de éxito en verde
    imprimir_color(f'✓ {mensaje}', 'VERDE')

def imprimir_error(mensaje):
    # Mensaje de error en rojo
    imprimir_color(f'✗ {mensaje}', 'ROJO')

def imprimir_info(mensaje):
    # Información en cyan
    imprimir_color(f'ℹ {mensaje}', 'CYAN')
            
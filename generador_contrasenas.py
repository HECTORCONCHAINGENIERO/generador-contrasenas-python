import random
import string

def generar_contrasena(longitud, usar_mayusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ""
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        return "Error: Debes seleccionar al menos un tipo de carácter."
    
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Menú para el usuario
print("=== Generador de Contraseñas Seguras ===")
longitud = int(input("Ingresa la longitud deseada para la contraseña: "))
usar_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
usar_minus = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
usar_nums = input("¿Incluir números? (s/n): ").lower() == 's'
usar_simb = input("¿Incluir símbolos? (s/n): ").lower() == 's'

nueva_contrasena = generar_contrasena(longitud, usar_mayus, usar_minus, usar_nums, usar_simb)
print(f"\nTu contraseña generada es: {nueva_contrasena}")
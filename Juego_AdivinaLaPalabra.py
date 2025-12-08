print("juego: EL COMPUTADOR ADIVINA TU PALABRA")
print("Piensa en una palabra (NO la escribas). Debe estar en la lista.\n")


palabras = ["sistema", "computadora", "python", "software", "codigo", "hardware", "web", "red"]

print("Lista de palabras posibles:")
print(palabras)
input("\nPresiona ENTER cuando estés listo...")


letras = list("abcdefghijklmnopqrstuvwxyz")


letras_encontradas = []
fallos = 0
maximo_fallos = 6
posibles = palabras.copy()

print("\nVoy a adivinar tu palabra preguntando letras.\n")


for letra in letras:

    
    if fallos >= maximo_fallos:
        break

    
    respuesta = input(f"¿Tu palabra contiene la letra '{letra}'? (Si/No): ").lower()

    
    if respuesta == "si":
        letras_encontradas.append(letra)
        posibles = [p for p in posibles if letra in p]
        print("Letra encontrada")

    
    else:
        fallos += 1
        print(f"Fallé. Intentos usados: {fallos}/{maximo_fallos}")
        posibles = [p for p in posibles if letra not in p]

    # Mostrar estado actual
    print("Palabras que podrían ser tu palabra:", posibles)

    # Si queda una sola palabra, ya se adivinó
    if len(posibles) == 1:
        print("\n¡Creo que ya sé cuál es tu palabra!")
        print(f"Tu palabra es: {posibles[0].upper()} 🎉")
        break

# Resultados finales
print("\nRESULTADOS")
if fallos >= maximo_fallos:
    print("No pude adivinar tu palabra. :(")
else:
    print("Juego finalizado.")

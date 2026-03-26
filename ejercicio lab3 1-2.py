# Lista de diccionarios
personas = [
    {"nombre": "gabo", "edad": 26},
    {"nombre": "dede", "edad": 27}
]

# Recorrer la lista
for persona in personas:
    print("\nPersona:")

    for clave, valor in persona.items():
        print(clave, ":", valor)
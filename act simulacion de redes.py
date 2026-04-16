class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []  # lista de nodos conectados

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def enviar_mensaje(self, mensaje):
        print(f"\n{self.nombre} envía: {mensaje}")
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje, self.nombre)

    def recibir_mensaje(self, mensaje, remitente):
        print(f"{self.nombre} recibió de {remitente}: {mensaje}")


# Crear nodos (1 servidor y 3 clientes)
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

# Conectar servidor con clientes
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

# Simular envío de mensaje
servidor.enviar_mensaje("Hola clientes, este es el servidor")
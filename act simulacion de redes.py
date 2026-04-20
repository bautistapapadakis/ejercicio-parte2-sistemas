class Nodo:
    def __init__(self, nombre):# define una funcion,init(cuando creás un objeto de la clase),self(objeto que estás creando),nombre(dato que le pasás al objeto)
        self.nombre = nombre #Guarda el valor del parámetro
        self.conexiones = []  #guarda una lista de conexiones

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def enviar_mensaje(self, mensaje):
        print(f"\n{self.nombre} envía: {mensaje}")
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje, self.nombre)

    def recibir_mensaje(self, mensaje, emisor):
        print(f"{self.nombre} recibió de {emisor}: {mensaje}")



servidor = Nodo("servidor")
cliente1 = Nodo("cliente 1")
cliente2 = Nodo("cliente 2")
cliente3 = Nodo("cliente 3")


servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)


servidor.enviar_mensaje("Hola clientes, este es el servidor")
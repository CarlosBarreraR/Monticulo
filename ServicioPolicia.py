class Persona:
    def __init__(self, nombre, edad, direccion, motivo, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.motivo = motivo
        self.gravedad = gravedad

    def __lt__(self, other):
        if self.gravedad == other.gravedad:
            if self.edad < 12 and other.edad >= 12:  
                return True
            elif self.edad >= 12 and other.edad < 12:
                return False
            elif self.edad > 65 and other.edad <= 65:
                return True
            elif self.edad <= 65 and other.edad > 65:
                return False
            else: 
                return self.edad < other.edad
        return self.gravedad < other.gravedad

class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.cola = 0

    def insertar(self,persona):
      self.listaMonticulo.append(persona)
      self.cola = self.cola + 1
      self.infiltArriba(self.cola)

    def infiltArriba(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i].gravedad < self.listaMonticulo[i // 2].gravedad:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            elif self.listaMonticulo[i].gravedad == self.listaMonticulo[i // 2].gravedad:
            # Si las gravedades son iguales, compara las edades para determinar la prioridad
                if self.listaMonticulo[i].edad < self.listaMonticulo[i // 2].edad:
                    tmp = self.listaMonticulo[i // 2]
                    self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                    self.listaMonticulo[i] = tmp
            i = i // 2

    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.cola]
        self.cola = self.cola - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def infiltAbajo(self,i):
      while (i * 2) <= self.cola:
          hm = self.hijoMin(i)
          if self.listaMonticulo[i] > self.listaMonticulo[hm]:
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.cola:
          return i * 2
      else:
          if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

class ServicioPolicial:
    def __init__(self):
        self.cola = MonticuloBinario()

    def ingresar_llamada(self, llamada):
        self.cola.insertar(llamada)
        posicion = self.cola.listaMonticulo.index(llamada)
        print(f"{llamada.nombre} ha sido ingresado en la cola y será atendido en la posición {posicion}.")

    def pasar_siguiente(self):
        return self.cola.eliminarMin()

    def mostrar_cola(self):
        self.cola.listaMonticulo[1:]
    

servicio = ServicioPolicial()

while True:
    print("1. Ingresar Llamada")
    print("2. Pasar siguiente solicitud")
    print("3. Mostrar la cola")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        direccion = input("Ingrese la dirección: ")
        motivo = input("Ingrese el motivo de la llamada: ")
        gravedad = int(input("Ingrese la gravedad (1-5): "))
        llamada = Persona(nombre, edad, direccion, motivo, gravedad)
        cola = servicio.mostrar_cola()
        servicio.ingresar_llamada(llamada)


    elif opcion == 2:
        siguiente = servicio.pasar_siguiente()
        if siguiente:
            print(f"La siguiente solicitud es de {siguiente.nombre}")
        else:
            print("No hay más solicitudes pendientes.")

    elif opcion == 3:
        cola = servicio.mostrar_cola()
        if cola:
            for posicion, llamada in enumerate(cola, start=1):
                print(f"\n{posicion}. {llamada.nombre}, {llamada.edad}, {llamada.direccion}, {llamada.motivo}, {llamada.gravedad}\n")
        else:
            print("La cola está vacía.")

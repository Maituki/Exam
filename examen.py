class Animal():
    def __init__(self, nombre, patas):
        self.nombre= nombre
        self.patas= patas
        

    def hacer_ruido(self):
         if self.nombre == "Perro":
             print(f"{self.nombre} woof woof")
         else:
              print(f"{self.nombre} tweet tweet")
    
              
class Perro(Animal):
    def __init__(self, nombre, patas, raza):
        #para acceder al padre ó madre poner SUPER
        super().__init__(nombre, patas)
        #si es un perro asigno por defecto valor 4. 
        self.__patas = 4
        self.raza=raza

    def correr(self):
        print("Estoy corriendo")   

class Pajaro(Animal):
    def __init__(self, nombre, patas):
        #para acceder al padre ó madre poner SUPER
        super().__init__(nombre, patas)
        #si es un ave asigno valor 2 
        self.__patas = 2

    def volar(self):
        # pendiente de definir - TO DO
        pass
        print("pendiente de realizar")

def imprimir_valores():
    #eliminamos los valores negativos de la lista
    lista = [5, 3, 12, -6, -3, 1, 6, 8, -12]
    list_aux =""
    for i in lista:
        if int(i) > 0:
            list_aux = list_aux + "," + str(i)
        #se imprime mensaje del número concreto 6
        if int(i) == 6:
            print("Hola número 6")
    print(list_aux)

def calcular_area (b,a):
    
    return b*a

if __name__=="__main__":

    b = float(input("inserta valor de la base del rectángulo "))
    a = input("inserta valor de la altura del rectángulo ")
    if a=="":
        print("valor de la altura")
    #     #si la base es 10 asignamos a la altura 3 por defecto
        x= calcular_area(b,3)
        
    else:
        a=float(a)
        x= calcular_area(b,a)
    print(x)

    #imprimir_valores()
    
    a= Animal("Pajaro",3)
    a.hacer_ruido()
    pj= Animal("Perro",4)
    pj.hacer_ruido()
    perro1= Perro("OK", 4, "Golden")
    perro1.correr()
    paja=Pajaro("may",2)
    paja.volar()

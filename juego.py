# #hijo prodigo - delia mamani
# nombre = input("Ingrese su nombre: ") #guardar lo que se escribe
# #variables
# dinero = 100
# dignidad = 50
# hambre = 0

# print(f"{nombre} ha recibido su herencia") #100
# print ("Que desea hacer con su herencia?")
# print ("1. Gastarlo todo en fiestas")
# print ("2. Invertir")
# print ("3. Ahorrar")

# opcion = int(input("Elige una opcion: "))
# if opcion == 1:
#     dinero = 0
#     dignidad -=20
#     hambre += 50
# elif opcion == 2:
#     dinero +=20
# elif opcion == 3:
#     print("Muy bien usted esta ahorrando") 
# else:
#     print("Esta opcion es invalida")      
    
# # gastar(dinero, dignidad)
# # trabajar(dinero, hambre)
# def gastar(dinero, dignidad):
#     dinero -= 30
#     dignidad -=10
#     return dinero, hambre

# def trabajar(dinero, hambre):
#     dinero += 15
#     hambre += 5
#     return dinero, hambre
    
# #bucle
# while dinero > 0:
#     print("“Sigues viviendo lejos de casa…”")
#     dinero -= 10
# -------------OBJETOS
# HijoProdigo
# Debe incluir:
# Atributos:
# nombre
# dinero
# dignidad
# hambre
# arrepentimiento
# -------------OBJETOS 
# HijoProdigo

class HijoProdigo: 
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0 

    def gastar_todo(self):
        if self.dinero >= 30:
            self.dinero -= 30
            self.dignidad -= 10
            self.hambre += 20
            print("Gastaste dinero en fiestas...")
        else:
            print("No tienes suficiente dinero.")

    def invertir(self):
        self.dinero += 20
        print("Invertiste sabiamente y ganaste dinero.")
        
    def ahorrar(self):
        print("Decidiste no gastar tu dinero.")
        
    def trabajar(self):
        self.dinero += 15
        self.hambre += 5
        print("Trabajaste duro y ganaste dinero.")
    
    def reflexionar(self):
        if self.hambre > 40:
            self.arrepentimiento += 10

    def mostrar_estado(self):
        print("\n--- ESTADO ACTUAL ---")
        print("Dinero:", self.dinero)
        print("Dignidad:", self.dignidad)
        print("Hambre:", self.hambre)
        print("Arrepentimiento:", self.arrepentimiento)
        print("----------------------")


# Crear jugador
jugador = HijoProdigo(input("Ingrese su nombre: "))

print(f"\n{jugador.nombre} ha recibido su herencia")
print(f"Dinero inicial: {jugador.dinero}")
print(f"Dignidad inicial: {jugador.dignidad}")
print(f"Hambre inicial: {jugador.hambre}")

# -------- BUCLE DEL JUEGO --------
while jugador.dinero > 0 and jugador.hambre < 100:

    jugador.mostrar_estado()

    print("\n¿Qué deseas hacer?")
    print("1. Gastar en fiestas")
    print("2. Invertir")
    print("3. Trabajar")
    print("4. Ahorrar")
    print("5. Salir del juego")

    try:
        opcion = int(input("Elige una opcion: "))
    except:
        print("Debes ingresar un número.")
        continue

    if opcion == 1:
        jugador.gastar_todo()
    elif opcion == 2:
        jugador.invertir()
    elif opcion == 3:
        jugador.trabajar()
    elif opcion == 4:
        jugador.ahorrar()
    elif opcion == 5:
        break
    else:
        print("Opción inválida")

    # Cada turno aumenta un poco el hambre
    jugador.hambre += 5

    jugador.reflexionar()

# -------- FINAL --------
print("\n===== FINAL DEL JUEGO =====")

if jugador.hambre >= 100:
    print("Muriste de hambre lejos de casa...")
elif jugador.dinero <= 0:
    print("Se acabó todo tu dinero.")
else:
    print("Decidiste abandonar tu vida lejos de casa.")

print("Arrepentimiento final:", jugador.arrepentimiento)

if jugador.arrepentimiento >= 20:
    print("Volviste a casa arrepentido y fuiste perdonado.")
else:
    print("Aún no aprendiste la lección.")

 

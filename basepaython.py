"""
nombre = "matias"
edad = 33
aprendo_python = True


base = 5
altura = 2
area = base * altura
print (f"El area calculada es: {area}")

temperatura = 20

if temperatura >= 18:
    print("hace calor")
else:
    print("hace frio")

for i in range(10):
    print("iteracion",i+1)


def sumar (n1, n2):
    return n1+n2 # sumar() puede ser usada en cálculos sin depender de print().

resultado = sumar(4,2)

print("Resultado", resultado)

class Coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def caracteristicas(self):
        return f"La marca es {self.marca} y el modelo es {self.modelo}" #Podemos almacenar la información en una variable y usarla más adelante.

coche1 = Coche("Peugeot","Active 1.6")        
print(coche1.caracteristicas())

"""
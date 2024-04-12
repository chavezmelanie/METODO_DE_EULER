#Hay un error dentro del código, marcado en el lugar que correpsonde, fijarse y corregirlo
#Escribe un codigo en Python que automatice el metodo de Euler para un problema de valor inicial apropiado para el metodo, dando la solucion en otro punto dado. Puedes
#utilizar un numero de pasos fijo, o variable, introducido por el usuario. En lo posible, la EDO puede ser tambien dada por el usuario.

import math

def euler(f, x0, y0, xf, h):
    x = x0
    y = y0
    while x < xf:
        y += h * f(x, y)
        x += h
    return y

# Ejercicio 1) Considera el problema con valor inicial dy/dx = 0,2 · x · y con y(1) = 1. Usa el programita para
# aproximar y(1.5) usando primero un paso de 0.1 y luego de 0.05.

def f1(x, y):
    return 0.2 * x * y

y_exacta_1 = math.exp(0.1 * 1.5**2) #chequear esta solución, tiene un error

# aproximacion con paso de 0.1
h = 0.1
y_aprox_1 = euler(f1, 1, 1, 1.5, h)
error_1 = abs(y_exacta_1 - y_aprox_1)

# aproximacion con paso de 0.05
h = 0.05
y_aprox_2 = euler(f1, 1, 1, 1.5, h)
error_2 = abs(y_exacta_1 - y_aprox_2)

print("Ejercicio 1:")
print(f"Solución exacta: {y_exacta_1}")
print(f"Aproximacion con paso de 0.1: {y_aprox_1}, Error: {error_1}")
print(f"Aproximacion con paso de 0.05: {y_aprox_2}, Error: {error_2}")


# Ejercicio 2)Considera un circuito simple donde la resistencia es 12 Ω, la inductancia es 4 H y la baterıa
#da un voltaje constante de 60 V. Si el interruptor esta cerrado cuando t = 0, se modela la corriente I en el tiempo t mediante el 
#problema con valores iniciales dI/dt = 15−3 ·I, I(0) = 0. Estima la corriente en el circuito medio segundo despues de que se cierra el interruptor.

def f2(t, I):
    return 15 - 3 * I

I_exacta = 5 - 5 * math.exp(-3 * 0.5)

# Aproximacion con paso de 0.1
h = 0.1
I_aprox = euler(f2, 0, 0, 0.5, h)
error_3 = abs(I_exacta - I_aprox)

print("\nEjercicio 2:")
print(f"Solución exacta: {I_exacta}")
print(f"La corriente en el circuito medio segundo después de cerrar el interruptor es aprox {I_aprox} amperios, Error: {error_3}")





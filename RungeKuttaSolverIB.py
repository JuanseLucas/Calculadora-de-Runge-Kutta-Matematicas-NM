import tkinter as tk
from tkinter import ttk, StringVar, IntVar, Text, Scrollbar
from math import sin
import time

# Definición de las ecuaciones diferenciales
def dydx1(x, y):
    return x

def dydx2(x, y):
    return (sin(x))**2

def dydx3(x, y):
    return 2*x**2 - 4*x**3

def dydx4(x, y):
    return x**5/y**5

# Método de Runge-Kutta
def rungeKutta(func, x0, y0, x, h):
    n = (int)((x - x0)/h)
    y = y0
    for i in range(1, n + 1):
        try:
            k1 = h * func(x0, y)
            k2 = h * func(x0 + 0.5 * h, y + 0.5 * k1)
            k3 = h * func(x0 + 0.5 * h, y + 0.5 * k2)
            k4 = h * func(x0 + h, y + k3)
            y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
        except OverflowError:
            results_text.insert(tk.END, f'Iteración {i}: Error de desbordamiento. El valor de y es demasiado grande.\n')
            break
        
        x0 = x0 + h
        results_text.insert(tk.END, f'Iteración {i}: y = {y}\n')
        time.sleep(0.5)
    return y


# Función para ejecutar el cálculo
def execute():
    functions = [dydx1, dydx2, dydx3, dydx4]
    start_time = time.time()
    for i, check in enumerate(check_values):
        if check.get():
            result = rungeKutta(functions[i], 0, 1, float(x_values[i].get()), float(h_values[i].get()))
            results_text.insert(tk.END, f'Resultado final para ecuación {i+1}: {result}\n')
    end_time = time.time()
    results_text.insert(tk.END, f'Tiempo de ejecución: {end_time - start_time} segundos\n')

# Crear la ventana principal
tk_root = tk.Tk()
tk_root.title('Runge-Kutta Solver')

# Variables para almacenar los valores de entrada
x_values = [StringVar() for _ in range(4)]
h_values = [StringVar() for _ in range(4)]
check_values = [IntVar() for _ in range(4)]

# Crear y colocar los widgets
labels = [
    'Ecuación 1: dy/dx = x',
    'Ecuación 2: dy/dx = sin^2(x)',
    'Ecuación 3: dy/dx = 2x^2 - 4x^3',
    'Ecuación 4: dy/dx = x^5/y^5'
]

for i, label in enumerate(labels):
    ttk.Label(tk_root, text=label).pack(pady=10)
    ttk.Checkbutton(tk_root, text='Seleccionar', variable=check_values[i]).pack()
    ttk.Label(tk_root, text='Valor de x:').pack()
    ttk.Entry(tk_root, textvariable=x_values[i]).pack()
    ttk.Label(tk_root, text='Valor de h:').pack()
    ttk.Entry(tk_root, textvariable=h_values[i]).pack()

execute_button = ttk.Button(tk_root, text='Ejecutar', command=execute)
execute_button.pack(pady=20)

# Agregar un widget Text para mostrar los resultados
results_text = Text(tk_root, wrap=tk.WORD, width=50, height=10)
results_text.pack(pady=20)
scrollbar = Scrollbar(tk_root, command=results_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
results_text.config(yscrollcommand=scrollbar.set)

# Iniciar el bucle principal de tkinter
tk_root.mainloop()

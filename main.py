import tkinter as tk
from tkinter import scrolledtext
import random
import requests


# Tu clave API de Hunter
api_key = ''

# Lista de sufijos y opciones de generación
sufijos = ["", ".", "_", "-", "1", "123", "99", "007", "x", "y", "z", "admin", "test", "contact", "support"]

# Lista para almacenar los correos generados
correos_generados = []

# Función para generar correos electrónicos
def generar_correos():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    dominio = dominio_entry.get()
    cantidad = int(cantidad_entry.get())
    
    for _ in range(cantidad):
        sufijo = random.choice(sufijos)
        correo = f"{nombre.lower()}{sufijo}{apellido.lower()}@{dominio}"
        #if verificar_correo(correo):
        correos_generados.append(correo)
    
    resultado_label.config(text=f"Generados {cantidad} correos:")
    actualizar_lista_correos()

# Función para verificar una dirección de correo electrónico utilizando la API de Hunter
#def verificar_correo(correo):
#    url = f'https://api.hunter.io/v2/email-verifier?email={correo}&api_key={api_key}'
#    response = requests.get(url)
#    data = response.json()
#    
#    return data['data']['result'] == 'valid'
#
# Función para actualizar la lista de correos generados
def actualizar_lista_correos():
    lista_correos.config(state=tk.NORMAL)
    lista_correos.delete(1.0, tk.END)  # Borra el contenido anterior
    for correo in correos_generados:
        lista_correos.insert(tk.END, correo + '\n')
    lista_correos.config(state=tk.DISABLED)
    guardar_correos()

# Función para guardar los correos generados en un archivo TXT
def guardar_correos():
    with open('correos_generados.txt', 'w') as archivo:
        for correo in correos_generados:
            archivo.write(correo + '\n')

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Generador de Correos Electrónicos")

# Etiquetas y campos de entrada
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(ventana)
nombre_entry.pack()

apellido_label = tk.Label(ventana, text="Apellido:")
apellido_label.pack()
apellido_entry = tk.Entry(ventana)
apellido_entry.pack()

dominio_label = tk.Label(ventana, text="Dominio:")
dominio_label.pack()
dominio_entry = tk.Entry(ventana)
dominio_entry.pack()

cantidad_label = tk.Label(ventana, text="Cantidad de Correos:")
cantidad_label.pack()
cantidad_entry = tk.Entry(ventana)
cantidad_entry.pack()

generar_button = tk.Button(ventana, text="Generar Correos Electrónicos", command=generar_correos)
generar_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Cuadro de texto con scroll para mostrar los correos generados
lista_correos = scrolledtext.ScrolledText(ventana, width=40, height=10, state=tk.DISABLED)
lista_correos.pack()

ventana.mainloop()

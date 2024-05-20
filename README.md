# Mail-Generator

Generador de Correos Electrónicos

Este programa genera direcciones de correo electrónico basadas en el nombre, apellido y dominio proporcionados. Utiliza la biblioteca tkinter para crear una interfaz gráfica de usuario (GUI) donde se pueden ingresar los datos necesarios y ver los correos generados.
Funcionalidades

    Generar múltiples correos electrónicos con combinaciones de sufijos predefinidos.
    Mostrar los correos generados en un cuadro de texto con desplazamiento.
    Guardar los correos generados en un archivo de texto.

Código

python

import tkinter as tk
from tkinter import scrolledtext
import random

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
        correos_generados.append(correo)
    
    resultado_label.config(text=f"Generados {cantidad} correos:")
    actualizar_lista_correos()

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

Uso

    Nombre: Ingrese el nombre de la persona.
    Apellido: Ingrese el apellido de la persona.
    Dominio: Ingrese el dominio del correo electrónico (por ejemplo, example.com).
    Cantidad de Correos: Ingrese la cantidad de correos electrónicos que desea generar.
    Generar Correos Electrónicos: Haga clic en el botón para generar los correos electrónicos.

Los correos generados se mostrarán en un cuadro de texto con desplazamiento y se guardarán en un archivo llamado correos_generados.txt.
Notas

    Los sufijos son seleccionados al azar de una lista predefinida para agregar variabilidad a los correos electrónicos.
    Actualmente, la verificación de correos electrónicos con la API de Hunter está desactivada. Si desea activarla, descomente la sección correspondiente del código y asegúrese de tener una clave API válida.

python

# Función para verificar una dirección de correo electrónico utilizando la API de Hunter
# def verificar_correo(correo):
#     url = f'https://api.hunter.io/v2/email-verifier?email={correo}&api_key={api_key}'
#     response = requests.get(url)
#     data = response.json()
#     
#     return data['data']['result'] == 'valid'

Requisitos

    Python 3.x
    tkinter (generalmente incluido con Python)
    requests (si se habilita la verificación de correos electrónicos)

Instalación de requests

Si no tiene el paquete requests instalado, puede instalarlo utilizando pip:

sh

pip install requests

Autor

    [Tu Nombre]
    Fecha: [Fecha]

Disfruta usando tu generador de correos electrónicos. Si tienes alguna pregunta o sugerencia, no dudes en contactarme.

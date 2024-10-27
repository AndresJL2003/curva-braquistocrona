import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("Mostrar Imágenes")

# Función para cerrar la ventana
def close_window():
    root.destroy()

# Función para cargar y mostrar una imagen
def show_image(image_path):
    # Limpiar cualquier imagen anterior
    label.config(image=None)
    
    # Cargar y mostrar la imagen
    image = Image.open(image_path)
    image = ImageTk.PhotoImage(image)
    label.config(image=image)
    label.image = image  # Conservar referencia para evitar que sea eliminada por el recolector de basura

# Función para mostrar el GIF animado
def show_gif():
    global frame_idx, gif_frames
    
    # Limpiar cualquier imagen anterior
    label.config(image=None)
    
    # Cargar el GIF y extraer sus frames
    gif_path = "corrida1.gif"
    gif = Image.open(gif_path)
    gif_frames = []
    try:
        while True:
            gif_frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass
    
    # Mostrar el primer frame inicialmente
    frame_idx = 0
    label.config(image=gif_frames[frame_idx])
    
    # Función para actualizar la imagen GIF
    def update_image():
        global frame_idx
        label.config(image=gif_frames[frame_idx])
        frame_idx = (frame_idx + 1) % len(gif_frames)
        label.after(100, update_image)  # Actualiza cada 100 milisegundos
    
    # Iniciar la animación del GIF
    update_image()

# Función para mostrar una imagen estática
def show_static_image():
    show_image("Captura de pantalla (12).png")

# Función para mostrar la imagen de tiempo
def show_time_image():
    show_image("tiempo.png")  # Reemplaza "tiempo.png" con la ruta de tu imagen de tiempo

# Cargar el logo y redimensionarlo
logo_path = "updslogo.png"
logo_img = Image.open(logo_path)
logo_img = logo_img.resize((logo_img.width // 2, logo_img.height // 2))  # Redimensionar a la mitad
logo_photo = ImageTk.PhotoImage(logo_img)

# Crear un widget de etiqueta para mostrar el logo encima de los botones
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack()

# Crear un widget de etiqueta para mostrar las imágenes
label = tk.Label(root)
label.pack()

# Botón para mostrar imagen GIF
btn_gif = tk.Button(root, text="Mostrar curva braquistocrona", command=show_gif)
btn_gif.pack(pady=10)

# Botón para mostrar imagen estática
btn_static = tk.Button(root, text="Mostrar Ecuaciones", command=show_static_image)
btn_static.pack(pady=10)

# Botón para mostrar la imagen de tiempo
btn_time = tk.Button(root, text="Mostrar Tiempo", command=show_time_image)
btn_time.pack(pady=10)

# Botón para salir
btn_exit = tk.Button(root, text="Salir", command=close_window)  
btn_exit.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()

import tkinter as tk

# Розміри вікна
WIDTH = 800
HEIGHT = 600

# Швидкість руху
SPEED = 5

# Створення головного вікна
root = tk.Tk()
root.title("Анімація зображення зліва направо")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Завантаження зображення (тільки .gif або .png без прозорості)
image = tk.PhotoImage(file="image.png")  # Заміни на image.png, якщо PNG простий
img_width = image.width()
img_height = image.height()

# Додавання зображення
img_id = canvas.create_image(-img_width // 2, HEIGHT // 2, anchor=tk.CENTER, image=image)

# Функція переміщення
def move():
    canvas.move(img_id, SPEED, 0)
    x, y = canvas.coords(img_id)
    if x - img_width // 2 > WIDTH:
        canvas.coords(img_id, -img_width // 2, HEIGHT // 2)
    root.after(30, move)

# Запуск
move()
root.mainloop()

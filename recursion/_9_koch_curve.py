import tkinter as tk
import math


class App:
    SCREEN_SIZE = (1920, 1080)
    WINDOW_SIZE = (700, 700)
    KOCH_COLOR = "blue"

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Кривая Коха")
        self.window.geometry("{size[0]}x{size[1]}+{left:.0f}+{top:.0f}".format(
            size=self.WINDOW_SIZE,
            left=(self.SCREEN_SIZE[0]-self.WINDOW_SIZE[0])/2,
            top=(self.SCREEN_SIZE[1]-self.WINDOW_SIZE[1])/2)
        )

        frame = tk.Frame(self.window)
        frame.pack()

        # Подпись.
        label = tk.Label(frame, text="Глубина:")
        label.pack(padx=5, pady=2, side=tk.LEFT)

        # Поле ввода глубины.
        self.depth_input = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.depth_input.pack(padx=5, pady=2, side=tk.LEFT)
        self.depth_input.insert(tk.END, "0")

        # Кнопка запуска метода.
        draw_button = tk.Button(frame, text="Нарисовать", width=14, command=self.draw)
        draw_button.pack(padx=(10, 5), pady=2, side=tk.LEFT)

        # Канва для рисования.
        frame = tk.Frame(self.window, borderwidth=3, relief="ridge")
        frame.pack(padx=5, pady=(0, 5), side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(frame, bg="white")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Выделяем поле ввода.
        self.depth_input.focus_force()
        self.depth_input.selection_from(0)
        self.depth_input.selection_to(1)
        self.window.mainloop()

    def draw(self):
        """
        Нарисовать кривую Коха.
        """

        # Получаем глубину.
        depth = int(self.depth_input.get())

        # Очищаем канву.
        self.canvas.delete(tk.ALL)

        # Вычисляем область рисования кривой.
        margin = 20
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        area_width = canvas_width - 2 * margin

        # Начальная точка для построения кривой.
        start_point = (margin, canvas_height / 2)

        # Запускаем алгоритм.
        self.draw_koch(depth, start_point, 0, koch_length=area_width)

        # Выделяем поле ввода.
        self.depth_input.selection_from(0)
        self.depth_input.selection_to(1)

    def draw_koch(self, depth, start_point, angle, koch_length):
        """
        Рекурсивный метод для рисования кривой Коха.
        """
        if depth == 0:
            end_point = (
                start_point[0] + koch_length * math.cos(angle),
                start_point[1] + koch_length * math.sin(angle)
            )
            self.canvas.create_line(
                start_point[0], start_point[1],
                end_point[0], end_point[1],
                fill=self.KOCH_COLOR
            )
        else:
            # Уменьшаем длину в 3 раза.
            new_length = koch_length / 3

            start_point_2 = (
                start_point[0] + new_length * math.cos(angle),
                start_point[1] + new_length * math.sin(angle)
            )

            theta1 = angle - math.pi / 3
            theta2 = angle + math.pi / 3

            start_point_3 = (
                start_point_2[0] + new_length * math.cos(theta1),
                start_point_2[1] + new_length * math.sin(theta1)
            )

            start_point_4 = (
                start_point_3[0] + new_length * math.cos(theta2),
                start_point_3[1] + new_length * math.sin(theta2)
            )

            self.draw_koch(depth - 1, start_point, angle, new_length)
            self.draw_koch(depth - 1, start_point_2, theta1, new_length)
            self.draw_koch(depth - 1, start_point_3, theta2, new_length)
            self.draw_koch(depth - 1, start_point_4, angle, new_length)


if __name__ == '__main__':
    app = App()
import tkinter as tk
from tkinter import ttk

class SimpleTimerApp:
    def __init__(self, root):
        self.root = root
        root.title("Простой Таймер")

        # Рамки для ввода времени
        time_input_frame = ttk.Frame(root)
        time_input_frame.pack(pady=10)

        ttk.Label(time_input_frame, text="Минуты:").grid(row=0, column=0, padx=5)
        self.minutes_entry = ttk.Entry(time_input_frame, width=5)
        self.minutes_entry.grid(row=0, column=1, padx=5)
        self.minutes_entry.insert(0, "0")

        ttk.Label(time_input_frame, text="Секунды:").grid(row=0, column=2, padx=5)
        self.seconds_entry = ttk.Entry(time_input_frame, width=5)
        self.seconds_entry.grid(row=0, column=3, padx=5)
        self.seconds_entry.insert(0, "0")

        # Отображение времени
        self.time_display = ttk.Label(root, text="00:00", font=("Helvetica", 48))
        self.time_display.pack(pady=10)

        # Шкала прогресса
        self.progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
        self.progress_bar.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTimerApp(root)
    root.mainloop()

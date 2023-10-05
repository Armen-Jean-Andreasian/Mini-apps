import tkinter as tk
from screenshot import take_screenshot


def run_gui():
    root = tk.Tk()
    root.geometry("160x30")

    root.iconbitmap('files/icon.ico')

    frame = tk.Frame(root)
    frame.pack()

    # screenshot
    button = tk.Button(
        frame,
        text='Take Screenshot',
        command=take_screenshot  # command takes id
    )
    button.pack(side=tk.LEFT)

    # exit
    close = tk.Button(
        frame,
        text='Exit',
        command=quit
    )
    close.pack(side=tk.RIGHT)

    root.mainloop()

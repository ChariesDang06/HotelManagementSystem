import tkinter as tk


def button(parent, text, command):
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        font=("Microsoft Sans Serif", 12),
        bg="linen",
        width=10,
    )
    return btn

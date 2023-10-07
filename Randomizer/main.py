import random
import tkinter as tk
from tkinter import messagebox


class RandomizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Randomizer")
        self.root.iconbitmap('files/icon.ico')
        self.root.resizable(width=False, height=False)

        self.names = []

        # Create and configure the entry widget
        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        # Create and configure the "Add an item" button
        self.add_button = tk.Button(root, text="Add an item", command=self.add_item)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Create and configure the "Pick a Random One" button
        self.pick_button = tk.Button(root, text="Pick a Random One", command=self.pick_random)
        self.pick_button.grid(row=1, column=0, padx=10, pady=10)

        # Create and configure the "Clean the list" button
        self.clean_button = tk.Button(root, text="Clean the list", command=self.clean_list)
        self.clean_button.grid(row=1, column=1, padx=10, pady=10)

    def add_item(self):
        user_input = self.entry.get()
        if user_input:
            self.names.append(user_input)
            self.entry.delete(0, tk.END)
            self.update_listbox()

    def pick_random(self):
        if len(self.names) < 2:
            messagebox.showwarning("Warning", "No names entered. Please enter at least two names.")
        else:
            random_name = random.choice(self.names)
            messagebox.showinfo("Random Name", random_name)
            self.clean_list()

    def clean_list(self):
        self.names = []
        self.update_listbox()

    def update_listbox(self):
        listbox.delete(0, tk.END)
        for index, item in enumerate(self.names, start=1):
            listbox.insert(tk.END, f"{index}: {item}")


if __name__ == '__main__':
    root_ = tk.Tk()
    app = RandomizerApp(root_)
    listbox = tk.Listbox(root_)
    listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    root_.mainloop()

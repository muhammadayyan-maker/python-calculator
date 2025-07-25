import tkinter as tk
from tkinter import messagebox
import math

# =============== FUNCTIONS =================
def click(event):
    global expression
    expression += str(event.widget["text"])
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    global expression
    try:
        result = eval(expression)
        history.append(expression + " = " + str(result))
        expression = str(result)
        input_text.set(expression)
        update_history()
    except:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""
        input_text.set("")

def update_history():
    history_box.delete(0, tk.END)
    for item in history[-5:][::-1]:
        history_box.insert(tk.END, item)

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    bg_color = "#222" if dark_mode else "white"
    fg_color = "white" if dark_mode else "black"
    entry.config(bg=bg_color, fg=fg_color, insertbackground=fg_color)
    for btn in buttons:
        btn.config(bg=bg_color, fg=fg_color)
    history_box.config(bg=bg_color, fg=fg_color)

# =============== GUI SETUP =================
root = tk.Tk()
root.title("ProPlus Calculator")
root.geometry("400x600")
root.resizable(False, False)

expression = ""
input_text = tk.StringVar()
history = []
dark_mode = False

entry = tk.Entry(root, textvariable=input_text, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify='right')
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Buttons Frame
btns_frame = tk.Frame(root)
btns_frame.pack()

buttons = []

btn_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "√", "x^y", "%"],
    ["n!", "π", "e", "Dark"]
]

for row in btn_texts:
    r_frame = tk.Frame(btns_frame)
    r_frame.pack(expand=True, fill="both")
    for text in row:
        def bind_click(x=text):
            if x == "=":
                return calculate()
            elif x == "C":
                return clear()
            elif x == "√":
                global expression
                expression = str(math.sqrt(float(expression)))
                input_text.set(expression)
            elif x == "x^y":
                expression += "**"
                input_text.set(expression)
            elif x == "%":
                expression += "%"
                input_text.set(expression)
            elif x == "n!":
                expression = str(math.factorial(int(expression)))
                input_text.set(expression)
            elif x == "π":
                expression += str(math.pi)
                input_text.set(expression)
            elif x == "e":
                expression += str(math.e)
                input_text.set(expression)
            elif x == "Dark":
                toggle_dark_mode()
            else:
                click({'widget': btn})

        btn = tk.Button(r_frame, text=text, font=("Arial", 18), relief=tk.RAISED, bd=4)
        btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)
        btn.bind("<Button-1>", click)
        buttons.append(btn)

# History
history_label = tk.Label(root, text="History", font=("Arial", 14))
history_label.pack(pady=(10, 0))
history_box = tk.Listbox(root, height=5, font=("Arial", 12))
history_box.pack(fill="both", padx=10, pady=5)

# =============== MAIN LOOP =================
root.mainloop()

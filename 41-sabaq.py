import tkinter as tk
from tkinter import messagebox
import math  
def calculate()
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END)     
    except Exception:
     messagebox.showerror("qate")
def sqrt_calc():         
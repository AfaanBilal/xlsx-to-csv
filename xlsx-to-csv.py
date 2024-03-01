#
# URL XLSX to CSV
# Download an XLSX file from the internet and convert and save it as a CSV in the downloads folder.
#
# Author: Afaan Bilal
# Link:   https://afaan.dev
#

import tkinter as tk
import urllib.request
import pandas as pd
import os
from pathlib import Path

filename = "file.xlsx"
csv_path = str(Path.home() / "Downloads") + "/file.csv"


def convert():
    urllib.request.urlretrieve(url.get(), filename)
    df = pd.read_excel(filename)
    df.to_csv(csv_path)
    os.remove(filename)


def clear():
    if os.path.isfile(csv_path):
        os.remove(csv_path)
    url.delete(0, tk.END)


window = tk.Tk()
window.title("URL XLSX to CSV")
window.geometry("500x50")
window.resizable(width=False, height=False)

frame = tk.Frame(master=window)
label = tk.Label(master=frame, text="URL: ")
url = tk.Entry(master=frame, width=50)

label.grid(row=0, column=0, sticky="e")
url.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="Run", command=convert, width=7)
btn_clear = tk.Button(master=window, text="Clear", command=clear, width=7)

frame.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
btn_clear.grid(row=0, column=2, padx=5, pady=10)

window.mainloop()

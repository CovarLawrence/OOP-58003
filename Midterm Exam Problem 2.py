import tkinter as tk

def convert():
    centimeters = float(entry_cm.get())
    meters = centimeters / 100.0
    kilometers = meters / 1000.0
    entry_m.delete(0, tk.END)
    entry_m.insert(0, "{:.2f}".format(meters))
    entry_km.delete(0, tk.END)
    entry_km.insert(0, "{:.2f}".format(kilometers))

root = tk.Tk()
root.title("Centimeters to Meters and Kilometers Converter")

label_cm = tk.Label(root, text="Enter the length in centimeters:")
label_cm.pack()

entry_cm = tk.Entry(root)
entry_cm.pack()

button = tk.Button(root, text="Convert", command=convert)
button.pack()

label_m = tk.Label(root, text="Length in meters:")
label_m.pack()

entry_m = tk.Entry(root)
entry_m.pack()

label_km = tk.Label(root, text="Length in kilometers:")
label_km.pack()

entry_km = tk.Entry(root)
entry_km.pack()

root.mainloop()

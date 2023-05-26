import datetime
import tkinter as tk
from tkinter import ttk


def record_mood():
    mood = mood_entry.get()
    today = datetime.date.today().strftime("%Y-%m-%d")
    with open("mood_tracker.txt", "a") as file:
        file.write(f"{today}: {mood}\n")
    mood_entry.delete(0, tk.END)
    status_label.config(text="Mood recorded successfully!")


def view_moods():
    with open("mood_tracker.txt", "r") as file:
        moods = file.readlines()
        moods_text = "\n".join(moods)
        mood_text.delete("1.0", tk.END)
        mood_text.insert(tk.END, moods_text)


# Create the main window
window = tk.Tk()
window.title("Mood Tracker")

# Create mood entry
mood_label = ttk.Label(window, text="Enter your mood:")
mood_label.pack()
mood_entry = ttk.Entry(window)
mood_entry.pack()

# Create record mood button
record_button = ttk.Button(window, text="Record Mood", command=record_mood)
record_button.pack()

# Create frame for displaying mood history
mood_frame = ttk.Frame(window)
mood_frame.pack()

# Create mood history label and scrollbar
history_label = ttk.Label(mood_frame, text="Mood History:")
history_label.pack()
scrollbar = ttk.Scrollbar(mood_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create text widget for mood history
mood_text = tk.Text(mood_frame, yscrollcommand=scrollbar.set)
mood_text.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=mood_text.yview)

# Create view mood button
view_button = ttk.Button(window, text="View Moods", command=view_moods)
view_button.pack()

# Create status label
status_label = ttk.Label(window, text="")
status_label.pack()

# Run the GUI main loop
window.mainloop()

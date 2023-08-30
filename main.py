import tkinter as tk
from tkinter import messagebox
import pyshorteners

def shorten_url():
    url = url_entry.get()
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        result_label.config(text="Shortened URL: " + short_url,foreground="green", font=("Helvetica", 24))
    except:
        messagebox.showerror("Error", "An error occurred while shortening the URL.")

# Create GUI window
window = tk.Tk()
window.title("URL Shortener")
window.geometry("600x400")
window.configure(bg="lightblue")

# Create GUI components
url_label = tk.Label(window, text="Enter URL:",font=("Helvetica",30))
url_entry = tk.Entry(window, width=40,font=("Helvetica",20))
shorten_button = tk.Button(window, text="Shorten",font=("Helvetica",24), command=shorten_url)
result_label = tk.Label(window, wraplength=300)

# Place components in the window
url_label.pack(pady=10)
url_entry.pack(pady=5)
shorten_button.pack(pady=5)
result_label.pack(pady=10)

# Start GUI event loop
window.mainloop()

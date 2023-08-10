#Jeopardy Game Test

import tkinter as tk
import Formatter

def open_game_window():
  main_window.destroy()
  window = tk.Tk()
  window.configure(bg="black")
  window.attributes('-fullscreen', False)

  # Configure rows and columns to expand
  for i in range(6):
      window.grid_rowconfigure(i, weight=1, uniform="row")
      window.grid_columnconfigure(i, weight=1, uniform="col")
      label = tk.Label(window, text=f"Category {i}", bg="#060CE9", fg="white")
      label.grid(row=0, column=i, padx=5, pady=12, sticky="nsew")

  for i in range(5):
      for j in range(6):
          button = tk.Button(window, text=f"Button {i+1}-{j+1}", bg="#060CE9", fg="white")
          button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

#create intro page
main_window = tk.Tk()
main_window.configure(bg="white")
main_window.attributes('-fullscreen', False)

label = tk.Label(text="Name")
label.pack()

entry = tk.Entry()
entry_val = entry.get()
entry.pack()

start_button = tk.Button(main_window, text="Play!", bg="#060CE9", fg="white", command=open_game_window)
start_button.pack()

main_window.mainloop()

print(entry_val)
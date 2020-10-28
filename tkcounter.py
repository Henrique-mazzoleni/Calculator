import tkinter as tk

counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text="Stop!", width=70, command=root.destroy)
button.pack()

#w = tk.Label(root, text="Hello Tkinter!", fg="blue", font="Times 20 italic")
#w.pack(side="right")

root.mainloop()

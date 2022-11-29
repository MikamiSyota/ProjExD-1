import tkinter as tk

root = tk.Tk()
r, c = 0, 0
for i in range(9, -1, -1):
    button = tk.Button(root, text=f"{i}", width=4, height=2, font=("",30))
    button.grid(row = r, column=c)
    #button.bind("<1>",button_click)
    c+=1
    if i%3==1:
        r+=1
        c=0
root.mainloop()
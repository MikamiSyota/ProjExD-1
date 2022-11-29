import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END, res)
    else:
        #tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
        entry.insert(tk.END, txt)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row = 0, column=0,columnspan=3)

r, c = 1, 0

command_list = ["c"]
for cm in command_list:
    button = tk.Button(root, text=cm, width=4, height=2, font=("",30))
    button.grid(row=r, column=c)
    c+=1
    if c%3 == 0:
        r += 1
        c = 0
    


r += 1
c = 0
for i in range(10):
    button = tk.Button(root, text=f"{9-i}", width=4, height=2, font=("",30))
    button.grid(row = r, column=c)
    button.bind("<1>",button_click)
    c+=1
    if i%3==2 and i != 0:
        r+=1
        c=0
        
ope = ["+", "="]
for op in ope:
    button = tk.Button(root, text=f"{op}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0
        

root.mainloop()
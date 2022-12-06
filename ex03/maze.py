import tkinter as tk
import maze_maker as mm

def add_command_list(cm):
    global command_list
    command_list.append(cm)
    
def check_command_list():
    global Flag, sFlag
    if command_list[-4::] == ["Up", "Left", "Down", "Right"]:
        Flag*=-1
    elif command_list[-6::] == ["Up","Up","Up","Up","Up","Up"]:
        sFlag *= -1

def key_down(event):
    global key, command_list, key
    key = event.keysym
    if key == "r":
        command_list = []
        key = ""
        reset_maze()
    add_command_list(key)
    
    
def key_up(event):
    global key
    key = ""
    check_command_list()
    
def reset_maze():
    global maze_list, mx, my, cx, cy, Flag, sFlag
    canvas.delete("koukaton")
    Flag = 1
    sFlag = 1
    mx, my = 1, 1
    cx, cy= mx*100+50, my*100+50
    maze_list = mm.make_maze(15, 9)
    #print(maze_list)
    mm.show_maze(canvas, maze_list)
    canvas.create_rectangle(100, 100, 200, 200, fill="yellow")
    canvas.create_rectangle(1300, 700, 1400, 800, fill="red")
    canvas.create_image(cx, cy, image=img, tag = "koukaton")
        
    
def main_proc():
    global cx, cy, mx, my, command_list, key, Flag
    if key == "Up": my -= 1
    elif key == "Down": my += 1
    elif key == "Left": mx -= 1
    elif key == "Right": mx += 1
    if maze_list[mx][my] == 1 and Flag == 1:
        if key == "Up": my += 1
        elif key == "Down": my -= 1
        elif key == "Left": mx += 1
        elif key == "Right": mx -= 1
    elif maze_list[mx][my] == 0 and Flag == -1:
        if key == "Up": my += 1
        elif key == "Down": my -= 1
        elif key == "Left": mx += 1
        elif key == "Right": mx -= 1
    cx, cy= mx*100+50, my*100+50
    canvas.coords("koukaton", cx, cy)
    if cx == 1350 and cy == 750:
        command_list = []
        key = ""
        reset_maze()
    if sFlag == -1:
        root.after(50,main_proc)
    else:
        root.after(100,main_proc) 
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    
    maze_list = mm.make_maze(15, 9)
    #print(maze_list)
    mm.show_maze(canvas, maze_list)
    canvas.create_rectangle(100, 100, 200, 200, fill="yellow")
    canvas.create_rectangle(1300, 700, 1400, 800, fill="red")

    
    img = tk.PhotoImage(file="./fig/8.png")
    sFlag = 1
    Flag = 1
    command_list = []
    mx, my = 1, 1
    cx, cy= mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=img, tag = "koukaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()
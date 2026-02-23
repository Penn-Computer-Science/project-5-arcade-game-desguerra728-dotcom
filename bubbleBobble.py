''']
3 lives
platform: player can jump up on them, cannot fall through them
enemies fall from top to the bottom, then move towards player
    same platform restrictions as player
    "angry mode"
shoot bubbles
    can jump over bubbles
catch enemies in bubble
    enemy in bubble floats up
    when enemy in bubble and player touches, enemy dies
    when enemy dead, drop food
    collect food, gain points
    higher points scores when bursting several bubbles at the same time
if touch enemy and not in bubble, dead
'''
import tkinter as tk

WIDTH = 600
HEIGHT = 450
PLATFORM_HEIGHT = 30
enemy_list = []
platform_list = []
player = None
canvas = None
def make_enemy_sprite():
    pattern = [
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == 0:
                img.put("#ff0000", (x,y))

    return img

def make_player_sprite():
    pattern = [
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == 0:
                img.put("#00fff2", (x,y))

    return img

def make_platform(width):
    h = PLATFORM_HEIGHT
    w = width

    img = tk.PhotoImage(width=w, height=h)
    for y in range(h):
        for x in range(w):
            img.put("#d978ff", (x,y))
    
    return img

def spawn_enemy(x_pos, y_pos):
    img = make_enemy_sprite()
    e = canvas.create_image(x_pos, y_pos, image=img, anchor="nw")
    enemy_list.append(e)

def spawn_player(x_pos, y_pos):
    global player
    img = make_player_sprite()
    player = canvas.create_image(x_pos, y_pos, image=img, anchor="center")

def place_platform(x_pos, y_pos, width):
    img = make_platform(width)
    p = canvas.create_image(x_pos, y_pos, image=img, anchor="center")
    platform_list.append(p)
    
def move_left(event):
    canvas.move(player, -15, 0)

def move_right(event):
    canvas.move(player, 15, 0)

def jump(event):
    canvas.move(player, 0, PLATFORM_HEIGHT+50)

root = tk.Tk()
root.title("Bubble Bobble")

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", jump)

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
spawn_player(WIDTH//2, HEIGHT//2)
img = make_player_sprite()
canvas.create_text(WIDTH//2, HEIGHT//2, text = "GAME OVER", fill = "red")
canvas.create_image(WIDTH//2, HEIGHT//2, image=img, anchor="center")
canvas.pack()
root.mainloop()

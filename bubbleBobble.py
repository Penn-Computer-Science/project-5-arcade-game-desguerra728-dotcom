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
isFacingLeft = True
WIDTH = 600
HEIGHT = 450
PLATFORM_HEIGHT = 25
enemy_list = []
platform_list = []
enemy_images = []
player_image = None
bubble_images = []
platform_img = []
root = tk.Tk()
root.title("Bubble Bobble")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()

player = canvas.create_image(0, 0)


def make_enemy_sprite():
    pattern = [
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "0":
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
        "00000000000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "0":
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

def make_bubble_sprite():
    pattern = ["00000000000",
               "00044444000",
               "00440000400",
               "00400400400",
               "00404000400",
               "00400000400",
               "00400000400",
               "00044444000",
               "00000000000"]
               
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "0":
                img.put("#000000", (x,y))
            else:
                img.put("#00d9ff")

    return img

def spawn_enemy(x_pos, y_pos):
    img = make_enemy_sprite()
    enemy_images.append(img)
    e = canvas.create_image(x_pos, y_pos, image=img, anchor="nw")
    enemy_list.append(e)

def spawn_player(x_pos, y_pos):
    global player
    global player_image
    pImg = make_player_sprite()
    player_image = pImg
    player = canvas.create_image(x_pos, y_pos, image=pImg, anchor="center")

def spawn_bubble(x_pos, y_pos):
    img = make_bubble_sprite()
    bubble_images.append(img)
    bubble = canvas.create_image(x_pos, y_pos, image=img, anchor="center")

def place_platform(x_pos, y_pos, width):
    img = make_platform(width)
    p = canvas.create_image(x_pos, y_pos, image=img, anchor="center")
    platform_img.append(img)
    platform_list.append(p)
    
def move_left(event):
    global isFacingLeft
    canvas.move(player, -15, 0)
    isFacingLeft = True

def move_right(event):
    global isFacingLeft
    canvas.move(player, 15, 0)
    isFacingLeft = False

def jump(event):
    canvas.move(player, 0, -PLATFORM_HEIGHT-30)

def shoot_bubble(event):
    spawn_bubble(canvas.coords(player)[0], canvas.coords(player)[1])
    if isFacingLeft:
        canvas.move(bubble_images[-1], -100, 0)


root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", jump)
root.bind("<b>", shoot_bubble)


spawn_enemy(100, 100)
place_platform(WIDTH//2, 400, 100)
place_platform(WIDTH//2+150, 350, 150)
place_platform(WIDTH//2-150, 350, 150)
place_platform(WIDTH//2+70, 300, 80)
place_platform(WIDTH//2-70, 300, 80)
place_platform(WIDTH//2+210, 300, 80)
place_platform(WIDTH//2-210, 300, 80)
spawn_player(WIDTH//2, 400-PLATFORM_HEIGHT//2-4)

root.mainloop()

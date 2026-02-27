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

tick = True
onPlatform = True

enemy_images = []
player_image = None
bubble_images = []
left_bubbles = []
right_bubbles = []
platform_img = []

root = tk.Tk()
root.title("Bubble Bobble")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()

player = canvas.create_image(0, 0)

isFacingLeft = True
def make_enemy_sprite():
    pattern = [
        "000000000000000000",
        "000000000000000000",
        "000222222222220000",
        "002222222222222000",
        "002222222222222000",
        "000022222222222000",
        "003302222222222000",
        "030030222222222000",
        "030030222220202000",
        "003302222220202000",
        "003302222220202000",
        "030035552222222000",
        "030035555555555500",
        "003314555555555500",
        "001114455555555000",
        "000011440014400000",
        "000000000111144000",
        "000000000000000000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "0":
                img.put("#000000", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ff8800", (x,y))
            elif pattern[y][x] == "3":
                img.put("#ffffff", (x,y))
            elif pattern[y][x] == "5":
                img.put("#ff0000", (x,y))
            elif pattern[y][x] == "4":
                img.put("#00d9ff", (x,y))
            elif pattern[y][x] == "1":
                img.put("#00ff15", (x,y))
    
    larger_img = img.zoom(2, 2)

    return larger_img

def make_player_sprite():
    pattern = [
        "000000005000000400",
        "000000055500004010",
        "000555555550000400",
        "000055111111100004",
        "000051111331130010",
        "055511113301033000",
        "005511113041043000",
        "000511113001003000",
        "055511113001003000",
        "005511553311133500",
        "000511001111111100",
        "000511110011100100",
        "000511111111111100",
        "000511111133330000",
        "005111113333333000",
        "055111133333333000",
        "511111222233323000",
        "111112223333222200"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "0":
                img.put("#000000", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ff8800", (x,y))
            elif pattern[y][x] == "3":
                img.put("#ffffff", (x,y))
            elif pattern[y][x] == "5":
                img.put("#ff0000", (x,y))
            elif pattern[y][x] == "4":
                img.put("#00d9ff", (x,y))
            elif pattern[y][x] == "1":
                img.put("#00ff15", (x,y))

    larger_img = img.zoom(2, 2)            

    return larger_img

def make_platform(width):
    h = PLATFORM_HEIGHT
    w = width

    img = tk.PhotoImage(width=w, height=h)
    for y in range(h):
        for x in range(w):
            img.put("#d978ff", (x,y))
    
    return img

def make_right_bub1():
    pattern = [
        "000000005000000400",
        "000000055500004010",
        "000555555550000400",
        "000055111111100004",
        "000051111331130010",
        "055511113301033000",
        "005511113041043000",
        "000511113001003000",
        "055511113001003000",
        "005511553311133500",
        "000511001111111100",
        "000511110011100100",
        "000511111111111100",
        "000511111133330000",
        "005111113333333000",
        "055111133333333000",
        "511111222233323000",
        "111112223333222200",]
               
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "0":
                img.put("#000000", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ff8800", (x,y))
            elif pattern[y][x] == "3":
                img.put("#ffffff", (x,y))
            elif pattern[y][x] == "5":
                img.put("#ff0000", (x,y))
            elif pattern[y][x] == "4":
                img.put("#00d9ff", (x,y))
            elif pattern[y][x] == "1":
                img.put("#00ff15", (x,y))

    larger_img = img.zoom(2, 2)            

    return larger_img

def make_right_bub2():
    pattern = [
        "000000005000000100",
        "000000055500004040",
        "000555555550000400",
        "000055111111100001",
        "000051111331130040",
        "055511113301033000",
        "005511113001003000",
        "000511113041043000",
        "055511113001003000",
        "005511553311133500",
        "000511001111111100",
        "000511110011100100",
        "000511111111111100",
        "000511111133330000",
        "005111113333333000",
        "055111133333333000",
        "511111222333322220",
        "111112222233222000"]
               
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "0":
                img.put("#000000", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ff8800", (x,y))
            elif pattern[y][x] == "3":
                img.put("#ffffff", (x,y))
            elif pattern[y][x] == "5":
                img.put("#ff0000", (x,y))
            elif pattern[y][x] == "4":
                img.put("#00d9ff", (x,y))
            elif pattern[y][x] == "1":
                img.put("#00ff15", (x,y))

    larger_img = img.zoom(2, 2)            

    return larger_img

def make_left_bub1():
    pattern = [
        "004000000500000000",
        "010400005550000000",
        "004000055555555000",
        "400001111111550000",
        "010031133111150000",
        "000330103311115550",
        "000340140311115500",
        "000300100311115000",
        "000300100311115550",
        "005331113355115500",
        "001111111100115000",
        "001001110011115000",
        "001111111111115000",
        "000033331111115000",
        "000333333311111500",
        "000333333331111550",
        "000323332222111115",
        "002222333322211111"]
               
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "0":
                img.put("#000000", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ff8800", (x,y))
            elif pattern[y][x] == "3":
                img.put("#ffffff", (x,y))
            elif pattern[y][x] == "5":
                img.put("#ff0000", (x,y))
            elif pattern[y][x] == "4":
                img.put("#00d9ff", (x,y))
            elif pattern[y][x] == "1":
                img.put("#00ff15", (x,y))

    larger_img = img.zoom(2, 2)            

    return larger_img

def make_left_bub2():
    pattern = [
        "001000000500000000",
        "040400005550000000",
        "004000055555555000",
        "100001111111550000",
        "040031133111150000",
        "000330103311115550",
        "000300100311115500",
        "000340140311115000",
        "000300100311115550",
        "005331113355115500",
        "001111111100115000",
        "001001110011115000",
        "001111111111115000",
        "000033331111115000",
        "000333333311111500",
        "000333333331111550",
        "022223333222111115",
        "000222332222211111",]
                   
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "0":
                img.put("#000000", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ff8800", (x,y))
            elif pattern[y][x] == "3":
                img.put("#ffffff", (x,y))
            elif pattern[y][x] == "5":
                img.put("#ff0000", (x,y))
            elif pattern[y][x] == "4":
                img.put("#00d9ff", (x,y))
            elif pattern[y][x] == "1":
                img.put("#00ff15", (x,y))

    larger_img = img.zoom(2, 2)            

    return larger_img

def make_bubble_sprite():
    pattern = ["000000000000000400",
        "000044444444440040",
        "000400000000004000",
        "004004040000000400",
        "040040000000000040",
        "040400000000040040",
        "040400000000004040",
        "040000000000004040",
        "040000000000000040",
        "040000000000000040",
        "040000000000000040",
        "040000000000000040",
        "040000000000000040",
        "040000000000000040",
        "004000000000000400",
        "400400000000004000",
        "000044444444440000",
        "004000000000000000"]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "0":
                img.put("#000000", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ff8800", (x,y))
            elif pattern[y][x] == "3":
                img.put("#ffffff", (x,y))
            elif pattern[y][x] == "5":
                img.put("#ff0000", (x,y))
            elif pattern[y][x] == "4":
                img.put("#00d9ff", (x,y))
            elif pattern[y][x] == "1":
                img.put("#00ff15", (x,y))

    larger_img = img.zoom(2, 2)

    return larger_img

def spawn_enemy(x_pos, y_pos):
    img = make_enemy_sprite()
    enemy_images.append(img)
    e = canvas.create_image(x_pos, y_pos, image=img, anchor="nw")
    enemy_list.append(e)

def spawn_player(x_pos, y_pos):
    global player
    global player_image
    pImg = make_left_bub1()
    player_image = pImg
    player = canvas.create_image(x_pos, y_pos, image=pImg, anchor="center")

def spawn_bubble(event):
    img = make_bubble_sprite()
    bubble_images.append(img)
    if isFacingLeft:
        bubble = canvas.create_image(canvas.coords(player)[0]-20, canvas.coords(player)[1], image=img, anchor="center")
        left_bubbles.append(bubble)
    else:
        bubble = canvas.create_image(canvas.coords(player)[0]+20, canvas.coords(player)[1], image=img, anchor="center")
        right_bubbles.append(bubble)

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

def animate_bub():
    global tick, onPlatform, player_image, player
    tick = not tick

    if isFacingLeft:
        if tick:
            new_img = make_left_bub1()
        else:
            new_img = make_left_bub2()
    else:
        if tick:
            new_img = make_right_bub1()
        else:
            new_img = make_right_bub2()

    player_image = new_img
    canvas.itemconfig(player, image=new_img)

    if right_bubbles:
        for b in right_bubbles:
            x1, y1, x2, y2 = canvas.bbox(b)
            if x2>WIDTH:
                canvas.delete(b)
                right_bubbles.remove(b)
            else:
                canvas.move(b, 10, 0)
    
    if left_bubbles:
        for b in left_bubbles:
            x1, y1, x2, y2 = canvas.bbox(b)
            if x2<0:
                canvas.delete(b)
                left_bubbles.remove(b)
            else:
                canvas.move(b, -10, 0)
    
    for p in platform_list:
        x1, y1, x2, y2 = canvas.bbox(p)
        px1, py1, px2, py2 = canvas.bbox(player)
        if x1<px2<x2 and y1==py2:
            onPlatform = True
        else:
            onPlatform = False



    root.after(100, animate_bub)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", jump)
root.bind("<space>", spawn_bubble)


spawn_enemy(100, 100)
place_platform(WIDTH//2, 400, 100)
place_platform(WIDTH//2+150, 350, 150)
place_platform(WIDTH//2-150, 350, 150)
place_platform(WIDTH//2+70, 300, 80)
place_platform(WIDTH//2-70, 300, 80)
place_platform(WIDTH//2+210, 300, 80)
place_platform(WIDTH//2-210, 300, 80)
spawn_player(WIDTH//2, 400-PLATFORM_HEIGHT//2-18)

animate_bub()

root.mainloop()

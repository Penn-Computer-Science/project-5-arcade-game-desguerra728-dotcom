import random
import tkinter as tk
isFacingLeft = True
WIDTH = 600
HEIGHT = 450
PLATFORM_HEIGHT = 25
enemy_list = []
platform_list = []
captured_enemy_list = []

counter = 1
points = 0
tick = True
onPlatform = True
alive = True
resetting = True
enemy_speed = 7
seen_controls = False

enemy_images = []
player_image = None
bubble_images = []
left_bubbles = []
right_bubbles = []
platform_img = []
captured_enemy_imgs = []
dead_img = None

root = tk.Tk()
root.title("Bubble Bobble")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()

player = canvas.create_image(0, 0)

isFacingLeft = True
eIsFacingLeft = False

def make_right_enemy1():
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

def make_right_enemy2():
    pattern = [
        "000000000000000000",
        "000000000000000000",
        "000000222222000000",
        "000222222222200000",
        "002222222222220000",
        "002222222222220000",
        "002222222202020000",
        "000200222202020000",
        "033033022202020000",
        "300300302222220000",
        "300300300000000000",
        "033033000000000000",
        "000500555555555000",
        "005555555555555000",
        "0055555555554144400",
        "000555555551444000",
        "000001440011110000",
        "000011114000000000"
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

def make_left_enemy1():
    pattern = [
        "000000000000000000",
        "000000000000000000",
        "000000000000000000",
        "000000222222222200",
        "000002222222222220",
        "000002222222222220",
        "000002222222222000",
        "000002222222220330",
        "000002222222203003",
        "000002020222203003",
        "000002020222220330",
        "000002020222220330",
        "000002222225553003",
        "000055555555553003",
        "000055555555541330",
        "000005555555441110",
        "000000044100411000",
        "000004411110000000"
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

def make_left_enemy2():
    pattern = [
        "000000000000000000",
        "000000000000000000",
        "000000222222000000",
        "000022222222222200",
        "000022222222222200",
        "000020202222222200",
        "000020202222002000",
        "000020202220330330",
        "000022222203003003",
        "000000000003003003",
        "000000000000330330",
        "000555555555005000",
        "000555555555555500",
        "0044144555555555500",
        "000444155555555000",
        "000011110044100000",
        "000011110044100000",
        "000000000411110000"
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

def make_captured_enemy_sprite1():
    pattern = ["004000000000000000",
        "040044444444440000",
        "000400000000004000",
        "004004242220000400",
        "040042422202000040",
        "040042220220200040",
        "040022222022200040",
        "040422222222040040",
        "040322222200540040",
        "043032000005450040",
        "040303555555544040",
        "040030355555111040",
        "040403555550010040",
        "040040114400000040",
        "004004111400000400",
        "000400000000004040",
        "000044444444440404",
        "000000000000000040"]
    
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

def make_captured_enemy_sprite2():
    pattern = ["000400000000000000",
    "004044444444440000",
    "000400000000004000",
    "004000424222000400",
    "040004242220200040",
    "040004222022020040",
    "040002222202220040",
    "040042222222204040",
    "040032222220054040",
    "040303200000545040",
    "040030355555554440",
    "040003035555511140",
    "040040355555001040",
    "040004011440000040",
    "004000411140000400",
    "000400000000004004",
    "000044444444440040",
    "000000000000000004"]

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

def make_dead_p_sprite1():
    pattern = ["000000000000010000",
        "000004000004000000",
        "000000000000400000",
        "000000000010000010",
        "000000000000000400",
        "000100000000000000",
        "001040001000000000",
        "000400000400000000",
        "000000001000000000",
        "040000000000000000",
        "000000000000000000",
        "000000000000220000",
        "000111133331120000",
        "001111111111110000",
        "511111111111110000",
        "555555111111111100",
        "055515555555111550",
        "015111551551555510"]
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
    
def make_dead_p_sprite2():
    pattern = ["000000400000400000",
        "000000000000040000",
        "000000000001000001",
        "000000000000000040",
        "000010000000000000",
        "000104000100000000",
        "000040000040000000",
        "000000000100000000",
        "004000000000000000",
        "000000000000000000",
        "000000000000000000",
        "000000000000220000",
        "000111133331120000",
        "001111111111110000",
        "511111111111110000",
        "555555111111111100",
        "055515555555111550",
        "015111551551555510"]

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
    img = make_right_enemy1()
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
    if len(right_bubbles) + len(left_bubbles) < 5:
        img = make_bubble_sprite()
        bubble_images.append(img)
        if alive:
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
    if alive:
        canvas.move(player, -22, 0)
        isFacingLeft = True

def move_right(event):
    global isFacingLeft
    if alive:
        canvas.move(player, 22, 0)
        isFacingLeft = False

def jump(event):
    if onPlatform and alive:
        canvas.move(player, 0, -PLATFORM_HEIGHT-70)

def spawn_captured_enemy(x_pos, y_pos):
    img = make_captured_enemy_sprite1()
    captured_enemy_imgs.append(img)
    ce = canvas.create_image(x_pos, y_pos, image=img, anchor="center")
    captured_enemy_list.append(ce)

def game_loop():
    global tick, onPlatform, player_image, player, enemy_images, enemy_list, eIsFacingLeft, counter, points, alive, enemy_speed
    tick = not tick
    if resetting == True:
        return

    j = points//10

    if counter == 0:
        for i in range(j-2):
            spawn_enemy(random.randint(0, WIDTH-50), 0)
    elif  not enemy_list:
        for i in range(j):
            spawn_enemy(random.randint(0, WIDTH-50), -15)
    

    canvas.create_rectangle(0, 0, WIDTH, 30, fill="#240141")
    canvas.create_text(50, 15, text = "SCORE: " + str(points), fill = "#ffffff", font = ("Arial", 12, "bold"))

    px1, py1, px2, py2 = canvas.bbox(player)

    enemy_speed = 7 + points/10
    
    if counter>10000//60:
        counter = 0
    else:
        counter += 1

    if alive:
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

    else:
        if tick:
            new_img = make_dead_p_sprite1()
        else:
            new_img = make_dead_p_sprite2()

    player_image = new_img
    canvas.itemconfig(player, image=new_img)

    if right_bubbles:
        for b in right_bubbles:
            x1, y1, x2, y2 = canvas.bbox(b)
            if x2>WIDTH:
                canvas.delete(b)
                right_bubbles.remove(b)
            else:
                canvas.move(b, 20, 0)

    if left_bubbles:
        for b in left_bubbles:
            x1, y1, x2, y2 = canvas.bbox(b)
            if x2<0:
                canvas.delete(b)
                left_bubbles.remove(b)
            else:
                canvas.move(b, -20, 0)

    for p in platform_list:
        lx1, ly1, lx2, ly2 = canvas.bbox(p)

        if (lx1<px1<lx2 or lx1<px2<lx2) and (ly1+5)>py2>(ly1-5):
            onPlatform = True
            break
        else:
            onPlatform = False

    if onPlatform == False:
        canvas.move(player, 0, 9)
    
    for e in enemy_list[:]:
        ex1, ey1, ex2, ey2 = canvas.bbox(e)
        eOnPlatform = False

        for p in platform_list:
            lx1, ly1, lx2, ly2 = canvas.bbox(p)
            if (lx1 < ex1 < lx2 or lx1 < ex2 < lx2) and (ly1 + 5) > ey2 > (ly1 - 5):
                eOnPlatform = True
                break

        if not eOnPlatform:
            canvas.move(e, 0, 9)

        ex1, ey1, ex2, ey2 = canvas.bbox(e)
        px1, py1, px2, py2 = canvas.bbox(player)

        if alive:
            if 0<counter<5000//60 and enemy_list.index(e)%2==0:
                if ex1 < px1:
                    canvas.move(e, -enemy_speed, 0)
                    eIsFacingLeft = True
                elif ex1 > px1:
                    canvas.move(e, enemy_speed, 0)
                    eIsFacingLeft = False
                
                if ey1 > py2:
                    canvas.move(e, 0, -PLATFORM_HEIGHT-70)
            else:
                if ex1 < px1:
                    canvas.move(e, enemy_speed, 0)
                    eIsFacingLeft = False
                elif ex1 > px1:
                    canvas.move(e, -enemy_speed, 0)
                    eIsFacingLeft = True
                
                if ey1 > py2:
                    canvas.move(e, 0, -PLATFORM_HEIGHT-70)
        else:
            canvas.move(e, -7, 0)
            eIsFacingLeft = True
        if ex2 < -50:
                canvas.coords(e, 600, ey1)
        elif ex1 > 650:
            canvas.coords(e, -600, ey1)

        if eIsFacingLeft:
            if tick:
                new_img = make_left_enemy1()
                canvas.itemconfig(e, image=new_img)
            else:
                new_img = make_left_enemy2()
                canvas.itemconfig(e, image=new_img)
        else:
            if tick:
                new_img = make_right_enemy1()
                canvas.itemconfig(e, image=new_img)
            else:
                new_img = make_right_enemy2()
                canvas.itemconfig(e, image=new_img)
        enemy_images.append(new_img)
        canvas.itemconfig(e, image=new_img)

        ex1, ey1, ex2, ey2 = canvas.bbox(e)
        for b in left_bubbles[:]:
            bx1, by1, bx2, by2 = canvas.bbox(b)
            if ex1<bx2<ex2 and (by1<ey2<by2 or by1<ey1<by2 or by1==ey1) and canvas.coords(e):
                canvas.delete(b)
                left_bubbles.remove(b)
                spawn_captured_enemy(canvas.coords(e)[0], canvas.coords(e)[1])
                canvas.delete(e)
                enemy_list.remove(e)

        for a in right_bubbles[:]:
            ax1, ay1, ax2, ay2 = canvas.bbox(a)
            if ex2>ax1>ex1 and (ay1<ey2<ay2 or ay1<ey1<ay2 or ay1==ey1) and canvas.coords(e):
                canvas.delete(a)
                right_bubbles.remove(a)
                spawn_captured_enemy(canvas.coords(e)[0], canvas.coords(e)[1])
                canvas.delete(e)
                enemy_list.remove(e)
        
        if (ex1<px1<ex2 or ex2<px2<ex1) and (ey1<py2<ey2 or ey1<py1<ey2 or py1==ey1):
            canvas.create_text(WIDTH//2, HEIGHT//2, text = "Game Over", fill = "#ff0000", font = ("Arial", 20, "bold"))
            alive = False
        
    if captured_enemy_list:
        for ce in captured_enemy_list:
            if tick:
                new_img = make_captured_enemy_sprite1()
            else:
                new_img = make_captured_enemy_sprite2()
            canvas.itemconfig(ce, image=new_img)
            captured_enemy_imgs.append(new_img)
            cx1, cy1, cx2, cy2 = canvas.bbox(ce)
            if cy1>30:
                canvas.move(ce, 0, -5)
        
            if (cx1<px2<cx2 or cx2>px1>cx1 or px1==cx1) and (py1<cy2<py2 or py1<cy1<py2 or py1==cy1):
                canvas.delete(ce)
                captured_enemy_list.remove(ce)
                points += 10

    if px1<-50:
        canvas.coords(player, 600, py1)
    if px2>650:
        canvas.coords(player, 0, py1)


    root.after(60, game_loop)

def reset():
    global seen_controls, alive, points, player_image, counter, resetting, bubble_images, left_bubbles, right_bubbles, enemy_images, enemy_list, captured_enemy_imgs, captured_enemy_list, platform_list
    if seen_controls == False:
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="Black")
        place_platform(WIDTH//4-30, 160, WIDTH//2-20)
        place_platform(WIDTH-WIDTH//4+30, 160, WIDTH//2-30)

        place_platform(WIDTH//4-30, 255, WIDTH//2-30)
        place_platform(WIDTH-WIDTH//4+30, 255, WIDTH//2-30)

        place_platform(WIDTH//4-30, 350, WIDTH//2-30)
        place_platform(WIDTH-WIDTH//4+30, 350, WIDTH//2-30)

        place_platform(WIDTH//2, HEIGHT-PLATFORM_HEIGHT//2, WIDTH*4) #bottom platform
        seen_controls = True

    if resetting:
        if alive == False:
            canvas.create_rectangle(0, HEIGHT//2+15, WIDTH, HEIGHT//2-20, fill="Black")

        alive = True
        points = 0
        counter = 1

        player_image = None
        
        if enemy_list:
            for e in enemy_list:
                canvas.delete(e)
        enemy_list.clear()
        enemy_images.clear()

        if captured_enemy_list:
            for ce in captured_enemy_list:
                canvas.delete(ce)
        captured_enemy_list.clear()
        captured_enemy_imgs.clear()

        if right_bubbles:
            for b in right_bubbles:
                canvas.delete(b)
        right_bubbles.clear()

        if left_bubbles:    
            for b in left_bubbles:
                canvas.delete(b)
        left_bubbles.clear()

        bubble_images.clear()

        spawn_enemy(25, 10)
        spawn_enemy(75, 10)
        spawn_player(WIDTH//2, 400-PLATFORM_HEIGHT//2-18)

    resetting = not resetting

    if resetting:
        reset_button.config(text = "Start Game", bg = "green")
    else:
        reset_button.config(text = "End Game", bg = "red")

    game_loop()

reset_button = tk.Button(root, text = "Start Game", command = reset, bg = "green", font = ("Courier", 10))
reset_button.pack()

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", jump)
root.bind("<space>", spawn_bubble)

canvas.create_text(WIDTH//2, 80, text="BuBBLE", fill="#ff00ea", font=("Arial Rounded MT Bold", 50, "bold"))
canvas.create_text(WIDTH//2, 132, text="BoBBLE", fill="#ff00ea", font=("Comic Sans MS", 50, "bold"))

canvas.create_text(WIDTH//2, 180, text="Capture the Bubble Busters in a", fill="#ffa857", font=("Ink Free", 15, "bold"))
canvas.create_text(WIDTH//2, 200, text="bubble before they catch you,", fill="#ffa857", font=("Ink Free", 15, "bold"))
canvas.create_text(WIDTH//2, 220, text="and pop them to earn points!", fill="#ffa857", font=("Ink Free", 15, "bold"))

canvas.create_text(WIDTH//2, 260, text="Controls:", fill="#ffffff", font=("Gabriola", 15, "bold"))
canvas.create_text(WIDTH//2, 280, text="← → to move", fill="#ffffff", font=("Gabriola", 15))
canvas.create_text(WIDTH//2, 300, text="↑ to jump", fill="#ffffff", font=("Gabriola", 15))
canvas.create_text(WIDTH//2, 320, text="Space-bar to shoot bubbles", fill="#ffffff", font=("Gabriola", 15))

canvas.create_text(WIDTH//2, 370, text="Click Start Game to Begin!", fill="#80fc8a", font=("MV Boli", 13))

root.mainloop()
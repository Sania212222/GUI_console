import math

print("\nConsole_gui: use point font 8x9 to make it work correctly\n")

n = 0
btns = []
full_block = "█"
mid_block_2 = "▓"
mid_block = "▒"
empety_block = "░"
def res_size(size_y = 20, size_x = 50):
    global size_of_window
    size_of_window = [size_x, size_y]
    
def previw_on():
    global preview
    preview = True
    
def initialization(type_fill_border=True, type_fill=True, block_b=1, block_f=4):
    global size_of_window
    global canvas
    
    if block_b == 1:
        block_b_2 = full_block
    elif block_b == 2:
        block_b_2 = mid_block_2
    elif block_b == 3:
        block_b_2 = mid_block
    elif block_b == 4:
        block_b_2 = empety_block
    
    if block_f == 1:
        block_f_2 = full_block
    elif block_f == 2:
        block_f_2 = mid_block_2
    elif block_f == 3:
        block_f_2 = mid_block
    elif block_f == 4:
        block_f_2 = empety_block
        
    if type_fill:
        canvas = [[block_f_2] * size_of_window[0] for i in range(size_of_window[1])]
    else:
        canvas = [[" "] * size_of_window[0] for i in range(size_of_window[1])]
    if type_fill_border:
        for i in range(size_of_window[0]):
            canvas[0][i] = block_b_2 
        for i in range(size_of_window[0]):
            canvas[len(canvas)-1][i] = block_b_2
        for i in range(size_of_window[1]-2):
            canvas[i+1][0] = block_b_2 
            canvas[i+1][len(canvas[len(canvas)-1])-1] = block_b_2
    

def line(coords_previous, coords_after, fill_block=1):
    lenght = 0
    x0, y0 = coords_previous
    x1, y1 = coords_after
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    sx = sy = 1
    if x0 > x1: sx = -1
    if y0 > y1: sy = -1
    err = dx - dy
    while True:
        draw_pixel([x0, y0], fill_block)
        if x0 == x1 and y0 == y1:
            return lenght
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
        lenght += 1

def sec_line(coords_after, coords_previous):
    lenght = 0
    x0, y0 = coords_previous
    x1, y1 = coords_after
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    sx = sy = 1
    if x0 > x1: sx = -1
    if y0 > y1: sy = -1
    err = dx - dy
    while True:
        draw_pixel([x0, y0], 1)
        if x0 == x1 and y0 == y1:
            return lenght
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def rect(coord_first, coord_last, type, fill_block=1):
    m = 0
    k = 0
    line(coord_first, [coord_last[0], coord_first[1]], fill_block) #left
    line(coord_first, [coord_first[0], coord_last[1]], fill_block) #up
    line(coord_last, [coord_last[0], coord_first[1]], fill_block) #down
    line(coord_last, [coord_first[0], coord_last[1]], fill_block) #right
    if fill_block == 1:
        full_block_2 = full_block
    if fill_block == 2:
        full_block_2 = mid_block_2
    if fill_block == 3:
        full_block_2 = mid_block
    if fill_block == 4:
        full_block_2 = empety_block
    if type == "f":
        flood_fill(coord_last[0]-2, coord_last[1]-2, mid_block, full_block_2, fill_block)

def circle(coords, r, type, type_two=False, fill_block=1):
    global n
    x = coords[0]
    y = coords[1]
    disp_x = x
    disp_y = y
    x = 0
    y = r
    delta = (1-2*r)
    error = 0
    while y >= 0:
        if type == "f":
            line([disp_x + x, disp_y + y], [disp_x - x, disp_y + y], fill_block)
            line([disp_x + x, disp_y - y], [disp_x - x, disp_y - y], fill_block)

            line([disp_x + y, disp_y + x], [disp_x - y, disp_y + x], fill_block)
            line([disp_x + y, disp_y - x], [disp_x - y, disp_y - x], fill_block)
            
        draw_pixel([disp_x + x, disp_y + y], fill_block)
        draw_pixel([disp_x - x, disp_y + y], fill_block)
        draw_pixel([disp_x + x, disp_y - y], fill_block)
        draw_pixel([disp_x - x, disp_y - y], fill_block)
        if type_two:
            draw_pixel([disp_x + y, disp_y + x], fill_block)
            draw_pixel([disp_x - y, disp_y + x], fill_block)
            draw_pixel([disp_x + y, disp_y - x], fill_block)
            draw_pixel([disp_x - y, disp_y - x], fill_block)
        
        error = 2 * (delta + y) - 1
        if ((delta < 0) and (error <=0)):
            x+=1
            delta = delta + (2*x+1)
            continue
        error = 2 * (delta - x) - 1
        if ((delta > 0) and (error > 0)):
            y -= 1
            delta = delta + (1 - 2 * y)
            continue
        x += 1
        delta = delta + (2 * (x - y))
        y -= 1
        
def draw_filled_polygon(center, sides, angle, radius, fill_block=1):
    x_center, y_center = center
    angle_rad = math.radians(angle)

    # Вычисляем координаты вершин многоугольника
    vertices = []
    for i in range(sides):
        x = x_center + radius * math.cos(angle_rad + 2 * math.pi * i / sides)
        y = y_center + radius * math.sin(angle_rad + 2 * math.pi * i / sides)
        vertices.append((x, y))

    # Находим границы многоугольника
    min_x = min(vertices, key=lambda p: p[0])[0]
    max_x = max(vertices, key=lambda p: p[0])[0]
    min_y = min(vertices, key=lambda p: p[1])[1]
    max_y = max(vertices, key=lambda p: p[1])[1]

    # Заполняем многоугольник по ребрам
    for y in range(int(min_y), int(max_y) + 1):
        intersections = []
        for i in range(sides):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % sides]

            # Проверяем горизонтальные рёбра многоугольника
            if (y1 < y <= y2) or (y2 < y <= y1):
                # Проверяем, что линия не находится полностью на горизонтальной линии
                if y1 != y2:
                    # Находим пересечения линии от (x1, y1) до (x2, y2) с горизонтальной линией y
                    x = x1 + (y - y1) / (y2 - y1) * (x2 - x1)
                    intersections.append(x)

        intersections.sort()
        for i in range(0, len(intersections), 2):
            x1 = max(min_x, min(intersections[i], max_x))
            x2 = max(min_x, min(intersections[min(i + 1, len(intersections) - 1)], max_x))
            line([int(x1), y], [int(x2), y], fill_block)
            
def polygon(center, sides, angle, radius, type, fill_block=1):
    if type == "e":
        x_center, y_center = center
        angle_rad = math.radians(angle)

        # Вычисляем координаты вершин многоугольника
        vertices = []
        for i in range(sides):
            x = x_center + int(radius * math.cos(angle_rad + 2 * math.pi * i / sides))
            y = y_center + int(radius * math.sin(angle_rad + 2 * math.pi * i / sides))
            vertices.append((x, y))
        for i in range(sides):
            line([vertices[i][0], vertices[i][1]], [vertices[(i + 1) % sides][0], vertices[(i + 1) % sides][1]], fill_block)
    if type == "f":
        draw_filled_polygon(center, sides, angle, radius, fill_block)

def flood_fill(x, y, fill_char, boundary_char, fill_block=1):
    stack = [(x, y)]

    while stack:
        current_x, current_y = stack.pop()
        if get_pixel([current_x, current_y]) != boundary_char and get_pixel([current_x, current_y]) != fill_char:
            draw_pixel([current_x, current_y], fill_block)
            stack.append((current_x + 1, current_y))
            stack.append((current_x - 1, current_y))
            stack.append((current_x, current_y + 1))
            stack.append((current_x, current_y - 1))

def free_polygon(coords, type, fill_block=1):
    f = 1
    
    if fill_block == 1:
        full_block_2 = full_block
    if fill_block == 2:
        full_block_2 = mid_block_2
    if fill_block == 3:
        full_block_2 = mid_block
    if fill_block == 4:
        full_block_2 = empety_block
        
    if type == "e":
        for i in range(len(coords)):
            try:
                line(coords[i], coords[f], fill_block)
            except:
                line(coords[0], coords[len(coords)-1], fill_block)
            f+=1
    if type == "f":
        for i in range(len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[(i + 1) % len(coords)]
            line([x1, y1], [x2, y2], fill_block)

        x_seed = sum(x for x, _ in coords) // len(coords)  # средняя координата x
        y_seed = sum(y for _, y in coords) // len(coords)  # средняя координата y
        flood_fill(x_seed, y_seed, mid_block, full_block_2, fill_block)

def draw_pixel(coords, fill_block=1):
    global canvas
    if fill_block == 1:
        block = full_block
    if fill_block == 2:
        block = mid_block_2
    if fill_block == 3:
        block = mid_block
    if fill_block == 4:
        block = empety_block
    canvas[coords[0]][coords[1]] = block
    
def char(coords, char, font="standart font", fill_block=1):
    x,y = coords
    if font == "standart font":
        if char == 'A':
            line(coords, [coords[0]-6, coords[1]+3], fill_block)
            line([coords[0]-6, coords[1]+3], [coords[0], coords[1]+6], fill_block)
            line([coords[0]-3, coords[1]+1], [coords[0]-3, coords[1]+5], fill_block)
            #draw_pixel(coords, 3)
        if char == 'B':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line([coords[0]-3, coords[1]+3], [coords[0]-3, coords[1]], fill_block)
            line([coords[0]-3, coords[1]+3], [coords[0], coords[1]+3], fill_block)
            line([coords[0], coords[1]+3], [coords[0], coords[1]], fill_block)
            #draw_pixel(coords, 3)
        if char == 'C':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line(coords, [coords[0], coords[1]+3], fill_block)
            line([coords[0]-6, coords[1]], [coords[0]-6, coords[1]+3], fill_block)
            
        if char == 'D':
            line([coords[0], coords[1]+3], [coords[0]-6, coords[1]+3], fill_block)
            line([coords[0]-3, coords[1]], [coords[0]-3, coords[1]+3], fill_block)
            line(coords, [coords[0]-3, coords[1]], fill_block)
            line([coords[0], coords[1]], [coords[0], coords[1]+3], fill_block)
            #draw_pixel(coords, 3)
        if char == 'E':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line(coords, [coords[0], coords[1]+3], fill_block)
            line([coords[0]-3, coords[1]], [coords[0]-3, coords[1]+3], fill_block)
            line([coords[0]-6, coords[1]], [coords[0]-6, coords[1]+3], fill_block)
        if char == 'F':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line([coords[0]-6, coords[1]], [coords[0]-6, coords[1]+3], fill_block)
            line([coords[0]-3, coords[1]+3], [coords[0]-3, coords[1]], fill_block)
            #draw_pixel(coords, 3)
        if char == 'G':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line([coords[0]-6, coords[1]], [coords[0]-6, coords[1]+4], fill_block)
            line([coords[0], coords[1]], [coords[0], coords[1]+4], fill_block)
            line([coords[0], coords[1]+4], [coords[0]-3, coords[1]+4], fill_block)
            line([coords[0]-3, coords[1]+4], [coords[0]-3, coords[1]+2], fill_block)
            #draw_pixel(coords, 3)
        if char == 'H':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line([coords[0], coords[1]+4], [coords[0]-6, coords[1]+4], fill_block)
            line([coords[0]-3, coords[1]], [coords[0]-3, coords[1]+4], fill_block)
        if char == 'I':
            line([coords[0], coords[1]+2], [coords[0]-6, coords[1]+2], fill_block)
        if char == 'J':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line(coords, [coords[0], coords[1]-3], fill_block)
        if char == 'L':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line(coords, [coords[0], coords[1]+3], fill_block)
        if char == 'M':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line([coords[0], coords[1]+6], [coords[0]-6, coords[1]+6], fill_block)
            line([coords[0]-6, coords[1]], [coords[0]-3, coords[1]+3], fill_block)
            line([coords[0]-3, coords[1]+3], [coords[0]-6, coords[1]+6], fill_block)
        if char == 'N':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line([coords[0], coords[1]+4], [coords[0]-6, coords[1]+4], fill_block)
            line([coords[0]-6, coords[1]], [coords[0], coords[1]+4], fill_block)
        if char == 'O':
            circle([coords[0]-3, coords[1]+2], 2, "e", False, fill_block)
        if char == 'P':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line([coords[0]-6, coords[1]], [coords[0]-6, coords[1]+3], fill_block)
            line([coords[0]-6, coords[1]+3], [coords[0]-3, coords[1]+3], fill_block)
            line([coords[0]-3, coords[1]+3], [coords[0]-3, coords[1]], fill_block)
            #draw_pixel(coords, 3)
        if char == 'Q':
            circle([coords[0]-3, coords[1]+2], 2, "e", False, fill_block)
            line([coords[0], coords[1]+3], [coords[0], coords[1]+5], fill_block)
        if char == 'R':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line([coords[0]-6, coords[1]], [coords[0]-6, coords[1]+3], fill_block)
            line([coords[0]-6, coords[1]+3], [coords[0]-3, coords[1]+3], fill_block)
            line([coords[0]-3, coords[1]+3], [coords[0]-3, coords[1]], fill_block)
            line([coords[0]-3, coords[1]], [coords[0], coords[1]+3], fill_block)
        if char == 'S':
            line([coords[0], coords[1]], [coords[0], coords[1]+3], fill_block)
            line([coords[0], coords[1]+3], [coords[0]-3, coords[1]+3], fill_block)
            line([coords[0]-3, coords[1]+3], [coords[0]-3, coords[1]], fill_block)
            line([coords[0]-3, coords[1]], [coords[0]-6, coords[1]], fill_block)
            line([coords[0]-6, coords[1]], [coords[0]-6, coords[1]+3], fill_block)
        if char == 'T':
            line([coords[0], coords[1]+2], [coords[0]-6, coords[1]+2], fill_block)
            line([coords[0]-6, coords[1]], [coords[0]-6, coords[1]+4], fill_block)
        if char == 'U':
            line(coords, [coords[0]-6, coords[1]], fill_block)
            line([coords[0], coords[1]+4], [coords[0]-6, coords[1]+4], fill_block)
            line([coords[0], coords[1]], [coords[0], coords[1]+4], fill_block)
        if char == 'V':
            line([coords[0]-6, coords[1]], [coords[0], coords[1]+2], fill_block)
            line([coords[0]-6, coords[1]+4], [coords[0], coords[1]+2], fill_block)
        if char == 'W':
            line([coords[0]-6, coords[1]], [coords[0], coords[1]+1], fill_block)
            line([coords[0], coords[1]+2], [coords[0]-6, coords[1]+3], fill_block)
            line([coords[0]-6, coords[1]+3], [coords[0], coords[1]+4], fill_block)
            line([coords[0], coords[1]+4], [coords[0]-6, coords[1]+5], fill_block)
        if char == 'X':
            line([coords[0], coords[1]], [coords[0]-6, coords[1]+5], fill_block)
            line([coords[0]-6, coords[1]], [coords[0], coords[1]+5], fill_block)
        if char == 'Y':
            line([coords[0], coords[1]], [coords[0]-6, coords[1]+5], fill_block)
            line([coords[0]-3, coords[1]+2], [coords[0]-6, coords[1]], fill_block)
        if char == 'Z':
            line([coords[0], coords[1]], [coords[0]-6, coords[1]+5], fill_block)
            line([coords[0], coords[1]], [coords[0], coords[1]+5], fill_block)
            line([coords[0]-6, coords[1]], [coords[0]-6, coords[1]+5], fill_block)
        if char == '!':
            draw_pixel(coords, fill_block)
            line([coords[0]-2, coords[1]], [coords[0]-6, coords[1]], fill_block)
        if char == '?':
            draw_pixel(coords, fill_block)
            line([coords[0]-2, coords[1]], [coords[0]-3, coords[1]], fill_block)
            line([coords[0]-3, coords[1]], [coords[0]-3, coords[1]+2], fill_block)
            line([coords[0]-3, coords[1]+2], [coords[0]-6, coords[1]+2], fill_block)
            line([coords[0]-6, coords[1]+2], [coords[0]-6, coords[1]], fill_block)
        if char == '.':
            draw_pixel(coords, fill_block)
        if char == ',':
            line([coords[0], coords[1]], [coords[0]+1, coords[1]], fill_block)
        if char == '<':
            line([coords[0]-3, coords[1]], [coords[0], coords[1]+4], fill_block)
            line([coords[0]-3, coords[1]], [coords[0]-6, coords[1]+4], fill_block)
        if char == '>':
            line([coords[0]-6, coords[1]], [coords[0]-3, coords[1]+4], fill_block)
            line([coords[0], coords[1]], [coords[0]-3, coords[1]+4], fill_block)
        if char == '_':
            line([coords[0], coords[1]], [coords[0], coords[1]+5], fill_block)
        if char == '-':
            line([coords[0]-3, coords[1]+1], [coords[0]-3, coords[1]+4], fill_block)
            
            
def string(coords_1, string, font="standart font", fill_block=1, type_fill_border_2=True):
    to_send = []
    j = 0
    pst = coords_1[1]
    for i in string:
        to_send.append(i)
    while j < len(to_send):
        try:
            if to_send[j] != " ":
                char(coords_1, to_send[j], font, fill_block)
            coords_1[1] += 7
            j+=1
        except:
            try:
                if type_fill_border_2:
                    char(coords_1, to_send[j], font, 1)
                else:
                    char(coords_1, to_send[j], font, 4)
            except:
                pass
            coords_1[0] += 10
            coords_1[1] = pst
        if j >= 10000:
            break

def button(coords, name, type_2, type="r", type_fill_border_2=True, type_of_fill=1):
    global btns
    need = 0
    y,x = coords
    symbols = ["└","┘","┌","┐","─","|"," "]
    canvas[y][x] = symbols[0]
    canvas[y-2][x] = symbols[2]
    canvas[y-2][x+2] = symbols[3]
    canvas[y][x+2] = symbols[1]
    canvas[y-1][x+1] = symbols[6]
    canvas[y][x+1] = symbols[4]
    canvas[y-2][x+1] = symbols[4]
    canvas[y-1][x] = symbols[5]
    canvas[y-1][x+2] = symbols[5]
    
    btns.append(name.upper())
    
    for i in name:
        need+=7.5
    need = int(need)

    if type_2:
        if type == "r":
            string([coords[0]+2, coords[1]+4], f"<{name.upper()}", "standart font", type_of_fill, type_fill_border_2)
        if type == "l":
            string([coords[0]+2, coords[1]-need-5], f"{name.upper()}>", "standart font", type_of_fill, type_fill_border_2)

def on_click():
    name_btn = input("Btn's name: ")
    for i in range(len(btns)):
        try:
            if name_btn == btns[i]:
                return name_btn
        except:
            pass
  
def get_pixel(coords):
    global canvas
    return canvas[coords[0]][coords[1]]

def send():
    global canvas
    out = ""
    for i in range(len(canvas)):
        for j in range(len(canvas[len(canvas)-1])):
            out+=canvas[i][j]
            out+=""
        out+="\n"
    print(out)
    
previw_on()

if preview:
    res_size(60, 100)
    initialization(type_fill=False)
    
    string([32, 13], "GUI CONSOLE", "standart font", 1, True)
    polygon(center=[45,15], sides=6, angle=37, radius=7, type="f", fill_block=3)
    polygon(center=[45,85], sides=6, angle=323, radius=7, type="e", fill_block=2)
    circle([45,50], 5, "f", False, 3)
    circle([45,65], 5, "e", False, 1)
    circle([45,35], 5, "e", False, 2)
    line([10,2], [17,7], 2)
    line([10,97], [17,92], 3)
    rect([5,40], [10, 60], "f", 2)
    rect([5,65], [10,70], "f", 3)
    rect([5,30], [10,35], "f", 3)
    button([18,40], "HI", True, "l", True, 2)
    button([18, 50], "GUI", True, "r", True, 2)
    send()
    

"""
Пример использования:

res_size(100,100)

initialization(type_fill_border=border, type_fill=True, block_b=1, block_f=4)

line([7,2], [7,7])
line([16,2], [25,7])

rect([2,2], [5,5], "e")
rect([2,10], [5,17], "f")

circle([14,30], 6, "f", True)
circle([14,15], 5, "e", False)

polygon(center=[30,15], sides=4, angle=35, radius=7, type="f")
polygon(center=[30,30], sides=4, angle=35, radius=7, type="e")

free_polygon([[10+40,10+30],[22+40,14+30],[16+40,32+30],[13+40,28+30],[15+40,17+30]], "f")
free_polygon([[10+70,10+30],[22+70,14+30],[16+70,32+30],[13+70,28+30],[15+70,17+30]], "e")

line([7,2], [7,7])
line([16,2], [25,7])

rect([2,2], [5,5], "e", fill_block=3)
rect([2,10], [5,17], "f")

circle([14,30], 6, "f", True, fill_block=2)
circle([14,15], 5, "e", False)

polygon(center=[30,15], sides=4, angle=35, radius=7, type="f", fill_block=2)
polygon(center=[30,30], sides=4, angle=35, radius=7, type="e")
polygon(center=[85,15], sides=3, angle=18, radius=10, type="e")
polygon(center=[85,85], sides=6, angle=78, radius=9, type="f")

#free_polygon([[10+40,10+30],[22+40,14+30],[16+40,32+30],[13+40,28+30],[15+40,17+30]], "f", 2)
free_polygon([[10+70,10+30],[22+70,14+30],[16+70,32+30],[13+70,28+30],[15+70,17+30]], "f")

char([60, 15], "Z")
string([10, 50], "CHIPI CHIPI CHAPA CHAPA RYWI RYWI RAWA RAWA", "standart font", 1, border)

button([70, 90], "Hello", True, "l", border)

send()

btn_state = on_click()

print(btn_state)

Прошу заметить, модуль НЕ всегда корректно работает (особенно это связано с заполнением фигур (а именно прямоугольников и свободных полигонов), т.е. это тут реализовано через костыли)

"""
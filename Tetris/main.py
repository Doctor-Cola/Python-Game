#导入轮子
from gamebase import *
from tkinter import messagebox
import tkinter as tk
import random


R = 20
C = 12
cell_size = 30
height = R*cell_size
width = C*cell_size
current_block = None
FPS = 150

shapes = {
    'O': [(-1,-1), (0,-1), (-1,0), (0,0)],
    'S': [(-1,0), (0,0), (0,-1), (1,-1)],
    'T': [(-1,0), (0,0), (0,-1), (1,0)],
    'I': [(0,1), (0,0), (0,-1), (0,-2)],
    'L': [(-1,0), (0,0), (-1,-1), (-1,-2)],
    'J': [(-1,0), (0,0), (0,-1), (0,-2)],
    'Z': [(-1,-1), (0,-1), (0,0), (1,0)]
}

shapesColor = {
    'O':'blue',
    'S':'red',
    'T':'yellow',
    'I':'green',
    'L':'purple',
    'J':'orange',
    'Z':'Cyan',
}

win = tk.Tk()

canvas = tk.Canvas(win, width=width, height=height)
canvas.pack()
block_list = []

def draw_board(canvas, block_list):
    for ri in range(R):
        for ci in range(C):
           cell_type = block_list[ri][ci]
           if cell_type:
               draw_cell_by_cr(canvas, ci, ri, shapesColor[cell_type])
           else:
               draw_cell_by_cr(canvas, ci, ri)

for i in range(R):
    i_row = ['' for j in range(C)]
    block_list.append(i_row)

draw_board(canvas,block_list)

def generate_new_block():
    kind = random.choice(list(shapes.keys()))
    cr = [C//2, 0]
    new_block = {
        'kind': kind,
        'cell_list': shapes[kind],
        'cr': cr
    }

    return new_block

def check_move(block, direction=[0,0]):
    cc, cr = block['cr']
    cell_list = block['cell_list']

    for cell in cell_list:
        cell_c, cell_r = cell
        c = cell_c + cc + direction[0]
        r = cell_r + cr + direction[1]

        if c<0 or c>=C or r>=R:
            return False

        if r >= 0 and block_list[r][c]:
            return False

    return True

def save_to_block_list(block):
    shape_type = block['kind']
    cc, cr = block['cr']
    cell_list = block['cell_list']

    for cell in cell_list:
        cell_c, cell_r = cell
        c = cell_c + cc
        r = cell_r + cr

        block_list[r][c] = shape_type


def horizontal_move_block(event):
    global current_block
    direction = [0,0]

    if event.keysym == 'Left':
        direction = [-1,0]

    elif event.keysym == 'Right':
        direction = [1,0]

    else:
        return

    if current_block is not None and check_move(current_block, direction):
        draw_block_move(canvas, current_block, direction)

score = 0
win.title('俄罗斯方块 当前得分: %s' % score)

def rotate_block(event):
    global current_block
    if current_block is None:
        return

    cell_list = current_block['cell_list']
    rotate_list = []
    for cell in cell_list:
        cell_c, cell_r = cell
        rotate_cell = [cell_r, -cell_c]
        rotate_list.append(rotate_cell)

    block_after_rotate = {
        'kind': current_block['kind'],
        'cell_list': rotate_list,
        'cr': current_block['cr']
    }

    if check_move(block_after_rotate):
        cc, cr = current_block['cr']
        draw_cells(canvas, cc, cr, current_block['cell_list'])
        draw_cells(canvas, cc, cr, rotate_list, shapesColor[current_block['kind']])
        current_block = block_after_rotate

def land(event):
    global current_block
    if current_block is None:
        return

    cell_list = current_block['cell_list']
    cc, cr = current_block['cr']
    min_height = R
    for cell in cell_list:
        cell_c, cell_r = cell
        c, r = cell_c + cc, cell_r + cr
        if block_list[r][c]:
            return

        h=0
        for ri in range(r+1, R):
            if block_list[ri][c]:
                break
            else:
                h += 1

        if h < min_height:
            min_height = h
    down = [0, min_height]
    if check_move(current_block, down):
        draw_block_move(canvas, current_block, down)

def check_row_complete(row):
    for cell in row:
        if cell == '':
            return False

    return True

def check_and_clear():
    global score
    has_complete_row = False
    for ri in range(len(block_list)):
        if check_row_complete(block_list[ri]):
            has_complete_row = True
            if ri > 0:
                for cur_ri in range(ri, 0, -1):
                    block_list[cur_ri] = block_list[cur_ri-1][:]
                block_list[0] = ['' for j in range(C)]
            else:
                block_list[ri] = ['' for j in range(C)]

            score += 10

    if has_complete_row:
        draw_board(canvas, block_list)

        win.title('俄罗斯方块 当前得分: %s' % score)


def gameLoop():
    win.update()

    global current_block
    if current_block is None:
        new_block = generate_new_block()
        draw_block_move(canvas, new_block)
        current_block = new_block

        if not check_move(current_block):
            messagebox.showinfo('Game Over!', '你的最终得分是: %s' % score)
            win.destroy()
            return

    else:
        if check_move(current_block, [0,1]):
            draw_block_move(canvas, current_block, [0,1])
        else:
            save_to_block_list(current_block)
            current_block = None

    check_and_clear()

    win.after(FPS, gameLoop)

current_block = None

canvas.focus_set()
canvas.bind('<KeyPress-Left>', horizontal_move_block)
canvas.bind('<KeyPress-Right>', horizontal_move_block)
canvas.bind('<KeyPress-Up>', rotate_block)
canvas.bind('<KeyPress-Down>', land)

gameLoop()
win.mainloop()

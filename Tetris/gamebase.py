import tkinter as tk

R = 20
C = 12
cell_size = 30
height = R*cell_size
width = C*cell_size

shapesColor = {
    'O':'blue',
    'S':'red',
    'T':'yellow',
    'I':'green',
    'L':'purple',
    'J':'orange',
    'Z':'Cyan',
}



def draw_cell_by_cr(canvas, c ,r, color='#CCCCCC'):
    x0 = c*cell_size
    y0 = r*cell_size

    x1 = c*cell_size + cell_size
    y1 = r*cell_size + cell_size
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='white', width=2)

def draw_cells(canvas, c, r, cell_list, color='#CCCCCC'):
    for cell in cell_list:
        cell_c, cell_r = cell
        ci = cell_c+c
        ri = cell_r+r
        if 0<=c<C and 0<=r<R:
            draw_cell_by_cr(canvas, ci, ri, color)

def draw_block_move(canvas, block, direction=[0, 0]):
    shape_type = block['kind']
    c, r = block['cr']
    cell_list = block['cell_list']

    draw_cells(canvas, c, r, cell_list)

    dc, dr = direction
    new_c, new_r = c+dc, r+dr
    block['cr'] = [new_c, new_r]
    draw_cells(canvas, new_c, new_r, cell_list, shapesColor[shape_type])



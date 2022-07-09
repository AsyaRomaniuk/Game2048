from tkinter import *
from tkinter.messagebox import showinfo
from random import randint, choices


def CreateGrid(master, row, column):
    grid_frame = Frame(master, bg="azure3")
    cells = []
    for r in range(row):
        for c in range(column):
            cell = Label(grid_frame, text="", width=4,
                         height=2, state="disabled",
                         font=("Arial", 20, "bold"),
                         relief="flat", bg='azure4')
            cell.r, cell.c = r, c
            cell.val = 0
            cell.grid(row=r, column=c, padx=4, pady=4)
            cells.append(cell)
    grid_frame.pack()
    return cells


def GetColor(val):
    if val in G_COLORS.keys():
        return G_COLORS[val]
    else:
        return ("black", "white")


def AnimateCellAppearence(cell, time, b, s):
    if s != 0:
        cell.config(font=("Arial", b // s, "bold"))
        root.after(time, lambda: AnimateCellAppearence(cell, time, b, s - 1))


def GameOver():
    root.unbind("w")
    root.unbind("<Up>")
    root.unbind("<Down>")
    root.unbind("s")
    root.unbind("<Left>")
    root.unbind("a")
    root.unbind("<Right>")
    root.unbind("d")
    showinfo("The end", "Game over!")


def isGameOver() -> bool:
    if (all([G_cells[i - 1].val != G_cells[i].val for i in range(1, len(G_cells), 2)])
            and all([G_cells[i].val != G_cells[i + G_ROW].val for i in range(len(G_cells) - G_ROW)])
    and all([G_cells[i].val != 0 for i in range(len(G_cells))])):
        return True
    else:
        return False


def FillRandCell(cells, val):
    global G_res
    f = True
    while f:
        r, c = randint(0, G_ROW - 1), randint(0, G_COLUMN - 1)
        for cell in cells:
            if cell.r == r and cell.c == c and cell.val == 0:
                f = False
                G_res += val
                lab1.config(text=f"{G_res}")
                cell.val = val
                ColorCell(cell)
                time = 50
                root.after(time, AnimateCellAppearence(cell, time, 20, 6))
                break


def GetCell(r, c):
    for cell in G_cells:
        if r == cell.r and c == cell.c:
            return cell


def ColorCell(cell):
    color = GetColor(cell.val)
    if cell.val != 0:
        cell.config(text=f"{cell.val}", bg=color[0], fg=color[1])
    else:
        cell.config(text="", bg=color[0], fg=color[1])


def MoveUp(event):
    global G_replaced
    G_replaced = False
    for r in range(G_ROW):
        cells = [GetCell(r, c) for c in range(G_COLUMN)]
        for cell in cells:
            if cell.val != 0:
                rr = r - 1
                if rr != -1:
                    nex_cell = GetCell(rr, cell.c)
                    if nex_cell.val == 0:
                        G_replaced = True
                        while rr > 0 and GetCell(rr - 1, cell.c).val == 0:
                            rr -= 1
                            nex_cell = GetCell(rr, cell.c)
                        if rr - 1 != -1:
                            nex_cell2 = GetCell(rr - 1, cell.c)
                            if nex_cell2.val == cell.val:
                                nex_cell2.val = 2 * nex_cell2.val
                                ColorCell(nex_cell2)
                                cell.val = 0
                                ColorCell(cell)
                                root.after(50, AnimateCellAppearence(nex_cell2, 50, 20, 6))
                            elif nex_cell2.val != cell.val and nex_cell2.val != 0:
                                nex_cell.val = cell.val
                                ColorCell(nex_cell)
                                cell.val = 0
                                ColorCell(cell)
                        else:
                            nex_cell.val = cell.val
                            ColorCell(nex_cell)
                            cell.val = 0
                            ColorCell(cell)
                    else:
                        if nex_cell.r == cell.r - 1 and nex_cell.val == cell.val:
                            G_replaced = True
                            nex_cell.val = 2 * nex_cell.val
                            ColorCell(nex_cell)
                            cell.val = 0
                            ColorCell(cell)
                            root.after(50, AnimateCellAppearence(nex_cell, 50, 20, 6))
    if G_replaced: FillRandCell(G_cells, choices((2, 4), (0.8, 0.2))[0])
    if isGameOver(): GameOver()


def MoveDown(event):
    global G_replaced
    G_replaced = False
    for r in range(G_ROW - 1, -1, -1):
        cells = [GetCell(r, c) for c in range(G_COLUMN)]
        for cell in cells:
            if cell.val != 0:
                rr = r + 1
                if rr != G_ROW:
                    nex_cell = GetCell(rr, cell.c)
                    if nex_cell.val == 0:
                        G_replaced = True
                        while rr < G_ROW - 1 and GetCell(rr + 1, cell.c).val == 0:
                            rr += 1
                            nex_cell = GetCell(rr, cell.c)
                        if rr + 1 != G_ROW:
                            nex_cell2 = GetCell(rr + 1, cell.c)
                            if nex_cell2.val == cell.val:
                                nex_cell2.val = 2 * nex_cell2.val
                                ColorCell(nex_cell2)
                                cell.val = 0
                                ColorCell(cell)
                                root.after(50, AnimateCellAppearence(nex_cell2, 50, 20, 6))
                            elif nex_cell2.val != cell.val and nex_cell2.val != 0:
                                nex_cell.val = cell.val
                                ColorCell(nex_cell)
                                cell.val = 0
                                ColorCell(cell)
                        else:
                            nex_cell.val = cell.val
                            ColorCell(nex_cell)
                            cell.val = 0
                            ColorCell(cell)
                    else:
                        if nex_cell.r == cell.r + 1 and nex_cell.val == cell.val:
                            G_replaced = True
                            nex_cell.val = 2 * nex_cell.val
                            ColorCell(nex_cell)
                            cell.val = 0
                            ColorCell(cell)
                            root.after(50, AnimateCellAppearence(nex_cell, 50, 20, 6))
    if G_replaced: FillRandCell(G_cells, choices((2, 4), (0.8, 0.2))[0])
    if isGameOver(): GameOver()


def MoveLeft(event):
    global G_replaced
    G_replaced = False
    for c in range(G_COLUMN):
        cells = [GetCell(r, c) for r in range(G_ROW)]
        for cell in cells:
            if cell.val != 0:
                cc = c - 1
                if cc != -1:
                    nex_cell = GetCell(cell.r, cc)
                    if nex_cell.val == 0:
                        G_replaced = True
                        while cc > 0 and GetCell(cell.r, cc - 1).val == 0:
                            cc -= 1
                            nex_cell = GetCell(cell.r, cc)
                        if cc - 1 != -1:
                            nex_cell2 = GetCell(cell.r, cc - 1)
                            if nex_cell2.val == cell.val:
                                nex_cell2.val = 2 * nex_cell2.val
                                ColorCell(nex_cell2)
                                cell.val = 0
                                ColorCell(cell)
                                root.after(50, AnimateCellAppearence(nex_cell2, 50, 20, 6))
                            elif nex_cell2.val != cell.val and nex_cell2.val != 0:
                                nex_cell.val = cell.val
                                ColorCell(nex_cell)
                                cell.val = 0
                                ColorCell(cell)
                        else:
                            nex_cell.val = cell.val
                            ColorCell(nex_cell)
                            cell.val = 0
                            ColorCell(cell)
                    else:
                        if nex_cell.c == cell.c - 1 and nex_cell.val == cell.val:
                            G_replaced = True
                            nex_cell.val = 2 * nex_cell.val
                            ColorCell(nex_cell)
                            cell.val = 0
                            ColorCell(cell)
                            root.after(50, AnimateCellAppearence(nex_cell, 50, 20, 6))
    if G_replaced: FillRandCell(G_cells, choices((2, 4), (0.8, 0.2))[0])
    if isGameOver(): GameOver()


def MoveRight(event):
    global G_replaced
    G_replaced = False
    for c in range(G_COLUMN - 1, -1, -1):
        cells = [GetCell(r, c) for r in range(G_ROW)]
        for cell in cells:
            if cell.val != 0:
                cc = c + 1
                if cc != G_COLUMN:
                    nex_cell = GetCell(cell.r, cc)
                    if nex_cell.val == 0:
                        G_replaced = True
                        while cc < G_COLUMN - 1 and GetCell(cell.r, cc + 1).val == 0:
                            cc += 1
                            nex_cell = GetCell(cell.r, cc)
                        if cc + 1 != G_COLUMN:
                            nex_cell2 = GetCell(cell.r, cc + 1)
                            if nex_cell2.val == cell.val:
                                nex_cell2.val = 2 * nex_cell2.val
                                ColorCell(nex_cell2)
                                cell.val = 0
                                ColorCell(cell)
                                root.after(50, AnimateCellAppearence(nex_cell2, 50, 20, 6))
                            elif nex_cell2.val != cell.val and nex_cell2.val != 0:
                                nex_cell.val = cell.val
                                ColorCell(nex_cell)
                                cell.val = 0
                                ColorCell(cell)
                        else:
                            nex_cell.val = cell.val
                            ColorCell(nex_cell)
                            cell.val = 0
                            ColorCell(cell)
                    else:
                        if nex_cell.c == cell.c + 1 and nex_cell.val == cell.val:
                            G_replaced = True
                            nex_cell.val = 2 * nex_cell.val
                            ColorCell(nex_cell)
                            cell.val = 0
                            ColorCell(cell)
                            root.after(50, AnimateCellAppearence(nex_cell, 50, 20, 6))
    if G_replaced: FillRandCell(G_cells, choices((2, 4), (0.8, 0.2))[0])
    if isGameOver(): GameOver()


if __name__ == "__main__":
    root = Tk()
    root.focus()
    root.title("2048")
    root.resizable(False, False)
    G_res = 0
    G_replaced = True
    G_COLORS = {0: ('azure4', '#000000'),
                2: ('#eee4da', '#776e65'),
                4: ('#ede0c8', '#f9f6f2'),
                8: ('#edc850', '#f9f6f2'),
                16: ('#edc53f', '#f9f6f2'),
                32: ('#f67c5f', '#f9f6f2'),
                64: ('#f65e3b', '#f9f6f2'),
                128: ('#edcf72', '#f9f6f2'),
                256: ('#edcc61', '#f9f6f2'),
                512: ('#f2b179', '#776e65'),
                1024: ('#f59563', '#f9f6f2'),
                2048: ('#edc22e', '#f9f6f2')}
    G_ROW, G_COLUMN = 4, 4
    lab1 = Label(root, text=f"{G_res}")
    lab1.pack()
    G_cells = CreateGrid(root, G_ROW, G_COLUMN)
    [FillRandCell(G_cells, choices((2, 4), (0.8, 0.2))[0]) for i in range(2)]
    root.bind("<Up>", MoveUp)
    root.bind("w", MoveUp)
    root.bind("<Down>", MoveDown)
    root.bind("s", MoveDown)
    root.bind("<Left>", MoveLeft)
    root.bind("a", MoveLeft)
    root.bind("<Right>", MoveRight)
    root.bind("d", MoveRight)
    root.mainloop()

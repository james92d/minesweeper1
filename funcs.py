from cfg import *


def deleteFromTopGrid(x, y):
    for i in top_grid:
        if x == i[0] and y == i[1]:
            top_grid.remove(i)


def convertPixelsToRowCols(x, y):
    x = int((x - 1) / square_plus2)
    y = int((y - 1) / square_plus2)
    return x, y


def convertRowColsToPixels(x, y):
    x = square_plus2 * x + 1
    y = square_plus2 * y + 1
    return x, y


def killSurroundingNumberedTiles(x, y):

    for e in range(1, 9):
        items = [[x - 1, y - 1, str(e)],
                 [x - 1, y, str(e)],
                 [x - 1, y + 1, str(e)],
                 [x, y - 1, str(e)],
                 [x, y + 1, str(e)],
                 [x + 1, y - 1, str(e)],
                 [x + 1, y, str(e)],
                 [x + 1, y + 1, str(e)]]

        for i in items:
            if i in full_grid:
                j = [i[0], i[1], 'top']
                if j in top_grid:
                    top_grid.remove(j)


def killSurroundingEmptyTiles(x, y):
    items = [[x - 1, y - 1, 'top'],
             [x - 1, y, 'top'],
             [x - 1, y + 1, 'top'],
             [x, y - 1, 'top'],
             [x, y + 1, 'top'],
             [x + 1, y - 1, 'top'],
             [x + 1, y, 'top'],
             [x + 1, y + 1, 'top']]

    for i in items:
        x = i[0]
        y = i[1]

        j = [x, y, '0']

        if i in top_grid:
            if j in full_grid:
                top_grid.remove(i)
                killSurroundingNumberedTiles(x, y)
                killSurroundingEmptyTiles(x, y)

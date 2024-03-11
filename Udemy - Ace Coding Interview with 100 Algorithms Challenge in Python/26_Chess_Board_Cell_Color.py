def get_color(coord):
    coord_row, coord_col = int(coord[1]), coord[0]

    if coord_row % 2 == 0:
        if coord_col in ["b", "d", "f", "h"]:
            color = "black"
        else:
            color = "white"
    else:
        if coord_col in ["b", "d", "f", "h"]:
            color = "white"
        else:
            color = "black"

    return color

def find_chess_board_cell_color(coord1, coord2):
    chess = {}

    if get_color(coord1) == get_color(coord2):
        return "Same Color"
    else:
        return "Not the Same Color"


if __name__ == "__main__":
    coord1, coord2 = "c5", "f4"
    res = find_chess_board_cell_color(coord1, coord2)
    print(res)

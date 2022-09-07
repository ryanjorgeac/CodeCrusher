
# def vLineAt(board: list, row: int, column: int) -> bool:
#     if row == 0:
#         if board[row][column] == board[row + 1][column]:
#             if board[row][column] == board[row + 2][column]:
#                 return True
#
#     if row == len(board) - 1 or row > 1:
#         if board[row][column] == board[row - 1][column]:
#             if board[row][column] == board[row - 2][column]:
#                 return True
#
#             elif row < len(board) - 2:
#                 if board[row][column] == board[row + 1][column]:
#                     return True
#
#         if row < len(board) - 2:
#             if board[row][column] == board[row + 1][column]:
#                 if board[row][column] == board[row + 2][column]:
#                     return True
#
#     if 1 == row < len(board) - 1:
#         if board[row][column] == board[row - 1][column]:
#             if board[row][column] == board[row + 1][column]:
#                 return True
#
#         if row < len(board) - 2:
#             if board[row][column] == board[row + 1][column]:
#                 if board[row][column] == board[row + 2][column]:
#                     return True
#
#     else:
#         return False

def vLineAt(board: list, row: int, column: int) -> bool:
    if row == 0 or row < len(board) - 2:
        if board[row][column] == board[row + 1][column]:
            if board[row][column] == board[row + 2][column]:
                return True

            elif row > 1:
                if board[row][column] == board[row - 1][column]:
                    return True

    if row == len(board) - 1 or row > 1:
        if board[row][column] == board[row - 1][column]:
            if board[row][column] == board[row - 2][column]:
                return True

    if 0 < row < len(board) - 1:
        if board[row][column] == board[row - 1][column]:
            if board[row][column] == board[row + 1][column]:
                return True

    else:
        return False

def test_vLineAt_element_top_of_line():
    x = [[1,2,3,4]
        ,[4,5,1,4]
        ,[7,8,1,4],
         [7,8,1,3],
         [7,8,1,3]]

    assert vLineAt(x, 0, 3)

def test_vLineAt_element_mid_of_line():
    x = [[1,2,3,3],
         [4,5,1,4],
         [7,8,1,4],
         [7,8,1,4],
         [7,8,1,3]]

    assert vLineAt(x, 2, 3)

def test_vLineAt_element_base_of_line():
    x = [[1,2,3,3],
         [4,5,1,3],
         [7,8,1,4],
         [7,8,1,4],
         [7,8,1,4]]

    assert vLineAt(x, 4, 3)

def test_vLineAt_element_top_of_line_false():
    x = [[1,2,3,4]
        ,[4,5,1,2]
        ,[7,8,1,3],
         [7,8,1,3],
         [7,8,1,3]]

    assert not vLineAt(x, 0, 3)

def test_vLineAt_element_mid_of_line_false():
    x = [[1,2,3,3],
         [4,5,1,4],
         [7,8,1,3],
         [7,8,1,4],
         [7,8,1,3]]

    assert not vLineAt(x, 2, 3)

def test_vLineAt_element_base_of_line_false():
    x = [[1,2,3,3],
         [4,5,1,3],
         [7,8,1,4],
         [7,8,1,9],
         [7,8,1,4]]

    assert not vLineAt(x, 4, 3)


if __name__ == "__main__":
    test_vLineAt_element_base_of_line()
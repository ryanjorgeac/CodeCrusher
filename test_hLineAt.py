def hLineAt(board: list, row: int, column: int) -> bool:
    if column == 0 or column < len(board[row]) - 2:
        if board[row][column] == board[row][column + 1]:
            if board[row][column] == board[row][column + 2]:
                return True

            elif column > 0:
                if board[row][column] == board[row][column - 1]:
                    return True

    if column == len(board[row]) - 1 or column > 1:
        if board[row][column] == board[row][column - 1]:
            if board[row][column] == board[row][column - 2]:
                return True

    if 0 < column < len(board[row]) - 1:
        if board[row][column] == board[row][column - 1]:
            if board[row][column] == board[row][column + 1]:
                return True

    else:
        return False


def test_hLineAt_from_beginning():
    x = [[1, 1, 1, 4]
        , [4, 5, 1, 4]
        , [7, 8, 1, 4],
         [7, 8, 1, 3],
         [7, 8, 1, 3]]

    assert hLineAt(x, 0, 0)

def test_hLineAt_from_middle():
    x = [[4, 1, 1, 1]
        , [4, 5, 1, 4]
        , [7, 8, 1, 4],
         [7, 8, 1, 3],
         [7, 8, 1, 3]]

    assert hLineAt(x, 0, 2)

def test_hLineAt_from_end():
    x = [[4, 1, 1, 1]
        , [4, 5, 1, 4]
        , [7, 4, 4, 4],
         [7, 8, 1, 3],
         [7, 8, 1, 3]]

    assert hLineAt(x, 2, 3)

def test_hLineAt_from_end_false():
    x = [[4, 1, 1, 1]
        , [4, 5, 1, 4]
        , [7, 8, 1, 4],
         [7, 8, 1, 3],
         [7, 8, 1, 3]]

    assert not hLineAt(x, 1, 3)

def test_hLineAt_from_middle_false():
    x = [[4, 1, 1, 1]
        , [4, 5, 1, 4]
        , [7, 8, 1, 4],
         [7, 8, 1, 3],
         [7, 8, 1, 3]]

    assert not hLineAt(x, 0, 0)

def test_hLineAt_from_beginning_false():
    x = [[1, 1, 1, 4]
        , [4, 5, 1, 4]
        , [7, 8, 1, 4],
         [7, 8, 1, 3],
         [7, 8, 1, 3]]

    assert not hLineAt(x, 3, 3)
"""Mooduli joka sisältää pelilogiikkaan liittyviä funktioita"""
import numpy
ORDER = [3,2,4,1,5,0,6]
def tie_check(board):
    """Funktio, joka laskee ja palauttaa boolean arvon riippuen onko pelilauta täynnä eli kaikki pelimerkit pelattu (tasapeli)"""
    full = True
    for x in range(0,7):
            if not column_full_check(board, x):
                full = False
    return full
def check_if_4(line):
    if line == [1,1,1,1]:
        return 1
    if line == [2,2,2,2]:
        return 2
    return -1
def win_check(board):
    """Funktio, joka laskee ja palauttaa arvon 1 jos keltainen voitti, 2 jos punainen voitti ja 0 jos kumpikaan ei voittanut"""
    horisontal = horisontal_check(board)
    vertical = vertical_check(board)
    upwards_diag = diagonal_upwards_check(board)
    downwards_diag = diagonal_downwards_check(board)
    if horisontal == 1 or vertical == 1 or upwards_diag == 1 or downwards_diag == 1:
        return 1
    if horisontal == 2 or vertical == 2 or upwards_diag == 2 or downwards_diag == 2:
        return 2
    return 0
def win_check_numbered(numbered_board):
    horisontal = horisontal_numbered_check(numbered_board)
    vertical = vertical_numbered_check(numbered_board)
    u_diagonal = upwards_diagonal_numbered_check(numbered_board)
    d_diagonal = downwards_diagonal_numbered_check(numbered_board)
    if horisontal == 1 or vertical == 1 or u_diagonal == 1 or d_diagonal == 1:
        return 1
    if horisontal == 2 or vertical == 2 or u_diagonal == 2 or d_diagonal == 2:
        return 2
    return 0
def horisontal_numbered_check(numbered_board):
    for y in range(5,-1,-1):
        row = numbered_board[y][:]
        for x in range(6,2,-1):
            horisontal = [row[x-3],row[x-2],row[x-1],row[x]]
            if check_if_4(horisontal) == 2:
                return 2
            if check_if_4(horisontal) == 1:
                return 1
    return 0
def vertical_numbered_check(numbered_board):
    n_board = numpy.array(numbered_board)
    for x in ORDER:
        col = n_board[:,x]
        for y in range(5,2,-1):
            vertical=[col[y-3],col[y-2],col[y-1],col[y]]
            if check_if_4(vertical) == 2:
                return 2
            if check_if_4(vertical) == 1:
                return 1
    return 0
def upwards_diagonal_numbered_check(numbered_board):
    for y in range(5,2,-1):
        for x in range(3,-1,-1):
            u_diagonal = [numbered_board[y][x],numbered_board[y-1][x+1],
                        numbered_board[y-2][x+2],numbered_board[y-3][x+3]]
            if check_if_4(u_diagonal) == 2:
                return 2
            if check_if_4(u_diagonal) == 1:
                return 1
    return 0
def downwards_diagonal_numbered_check(numbered_board):
    for y in range(5,2,-1):
        for x in range(3,7):
            d_diagonal = [numbered_board[y-3][x-3], numbered_board[y-2][x-2],
                        numbered_board[y-1][x-1], numbered_board[y][x]]
            if check_if_4(d_diagonal) == 2:
                return 2
            if check_if_4(d_diagonal) == 1:
                return 1
    return 0
def column_full_check(board, x):
    """Funktio, joka tarkistaa onko kyisenen sarake x täynnä. Palauttaa True jos on ja False jos ei."""
    if not board[0][x].is_empty():
        return True
    return False

def vertical_check(board):
    """Funktio, joka tarkistaa onko pelilaudalla voittoa pystyriveissä jommalla kummalla värillä. Funktio palauttaa 0
    jos voittoa ei ole, 1 jos keltainen voitti ja 2 jos punainen voitti."""
    for y in range(5,2,-1):
            for x in range(6,-1,-1):
                if board[y][x].is_yellow() and board[y-1][x].is_yellow() and board[y-2][x].is_yellow() and board[y-3][x].is_yellow():
                    return 1
                if board[y][x].is_red() and board[y-1][x].is_red() and board[y-2][x].is_red() and board[y-3][x].is_red():
                    return 2
    return 0

def horisontal_check(board):
    """Funktio, joka tarkistaa onko pelilaudalla voittoa vaakariveissä jommalla kummalla värillä. Funktio palauttaa 0
    jos voittoa ei ole, 1 jos keltainen voitti ja 2 jos punainen voitti."""
    for y in range(5,-1,-1):
            for x in range(6,2,-1):
                if board[y][x].is_yellow() and board[y][x-1].is_yellow() and board[y][x-2].is_yellow() and board[y][x-3].is_yellow():
                    return 1
                if board[y][x].is_red() and board[y][x-1].is_red() and board[y][x-2].is_red() and board[y][x-3].is_red():
                    return 2
    return 0

def diagonal_upwards_check(board):
    """Funktio, joka tarkistaa onko pelilaudalla voittoa viistoon ylöspäin (vasemmmalta katsottuna) jommalla kummalla värillä. Funktio palauttaa 0
    jos voittoa ei ole, 1 jos keltainen voitti ja 2 jos punainen voitti."""
    for y in range(5,2,-1):
            for x in range(3,-1,-1):
                if board[y][x].is_yellow() and board[y-1][x+1].is_yellow() and board[y-2][x+2].is_yellow() and board[y-3][x+3].is_yellow():
                    return 1
                if board[y][x].is_red() and board[y-1][x+1].is_red() and board[y-2][x+2].is_red() and board[y-3][x+3].is_red():
                    return 2
    return 0

def diagonal_downwards_check(board):
    """Funktio, joka tarkistaa onko pelilaudalla voittoa viistoon alaspäin (vasemmmalta katsottuna) jommalla kummalla värillä. Funktio palauttaa 0
    jos voittoa ei ole, 1 jos keltainen voitti ja 2 jos punainen voitti."""
    for y in range(5,2,-1):
            for x in range(6,2,-1):
                if board[y][x].is_yellow() and board[y-1][x-1].is_yellow() and board[y-2][x-2].is_yellow() and board[y-3][x-3].is_yellow():
                    return 1
                if board[y][x].is_red() and board[y-1][x-1].is_red() and board[y-2][x-2].is_red() and board[y-3][x-3].is_red():
                    return 2
    return 0
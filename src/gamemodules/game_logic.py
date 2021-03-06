"""Mooduli joka sisältää pelilogiikkaan liittyviä funktioita"""
import numpy
"""ORDER muuttuja on lista x-arvoja, joka kuvaa otollisimman järjestyksen käydä
läpi pelilaudan sarakkeet"""
ORDER = [3,2,4,1,5,0,6]
def tie_check(board):
    """Funktio, joka laskee ja palauttaa boolean arvon 
    riippuen onko pelilauta täynnä eli kaikki pelimerkit
    pelattu ilman voittoa (tasapeli)"""
    full = True
    for x in range(0,7):
            if not column_full_check(board, x):
                full = False
    return full
def check_if_4(line):
    """Tarkistaa, onko 4:n rivissä neljä samaa ja palauttaa
    lukuarvon sen mukaan kumman pelaajan nappulat on kyseessä tai
    -1 jos ei kumpikaan.
    """
    if line.count(1) == 4:
        return 1
    if line.count(2) == 4:
        return 2
    return -1
def win_check(board):
    """Tarkistaa voitot. Palauttaa lukuarvon sen mukaan kumpi voitti ja 0, jos ei kumpikaan."""
    horisontal = horisontal_check(board)
    vertical = vertical_check(board)
    u_diagonal = upwards_diagonal_check(board)
    d_diagonal = downwards_diagonal_check(board)
    if horisontal == 1 or vertical == 1 or u_diagonal == 1 or d_diagonal == 1:
        return 1
    if horisontal == 2 or vertical == 2 or u_diagonal == 2 or d_diagonal == 2:
        return 2
    return 0
def horisontal_check(board):
    """Tarkistaa onko 4 samaa vaakariveiltä."""
    for y in range(5,-1,-1):
        row = board[y][:]
        for x in range(6,2,-1):
            horisontal = [row[x-3],row[x-2],row[x-1],row[x]]
            if check_if_4(horisontal) == 2:
                return 2
            if check_if_4(horisontal) == 1:
                return 1
    return 0
def vertical_check(board):
    """Tarkistaa onko 4 samaa pysty riveiltä."""
    n_board = numpy.array(board)
    for x in ORDER:
        col = n_board[:,x]
        for y in range(5,2,-1):
            vertical=[col[y-3],col[y-2],col[y-1],col[y]]
            if check_if_4(vertical) == 2:
                return 2
            if check_if_4(vertical) == 1:
                return 1
    return 0
def upwards_diagonal_check(board):
    """Tarkistaa onko 4 samaa peräkkäin ylöspäin viistoon
    olevilta riveiltä."""
    for y in range(5,2,-1):
        for x in range(3,-1,-1):
            u_diagonal = [board[y][x],board[y-1][x+1],
                        board[y-2][x+2],board[y-3][x+3]]
            if check_if_4(u_diagonal) == 2:
                return 2
            if check_if_4(u_diagonal) == 1:
                return 1
    return 0
def downwards_diagonal_check(board):
    """Tarkistaa onko 4 samaa peräkkäin alaspäin viistoon
    olevilta riveiltä."""
    for y in range(5,2,-1):
        for x in range(3,7):
            d_diagonal = [board[y-3][x-3], board[y-2][x-2],
                        board[y-1][x-1], board[y][x]]
            if check_if_4(d_diagonal) == 2:
                return 2
            if check_if_4(d_diagonal) == 1:
                return 1
    return 0
def column_full_check(board, x):
    """Funktio, joka tarkistaa onko parametrina saadun x-arvon
    mukainen sarake täynnä. Palauttaa True jos on ja False jos ei."""
    if board[0][x] != 0:
        return True
    return False
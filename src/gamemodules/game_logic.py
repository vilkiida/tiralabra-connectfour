"""Mooduli joka sisältää pelilogiikkaan liittyviä funktioita"""
def tie_check(board):
    """Funktio, joka laskee ja palauttaa boolean arvon riippuen onko pelilauta täynnä eli kaikki pelimerkit pelattu (tasapeli)"""
    full = True
    for x in range(0,7):
            if not column_full_check(board, x):
                full = False
    return full

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
def column_full_check(board, x):
    """Funktio, joka tarkistaa onko kyisenen sarake x täynnä. Palauttaa True jos on ja False jos ei."""
    if not board[0][x].is_empty():
        return True
    return False

def horisontal_check(board):
    """Funktio, joka tarkistaa onko pelilaudalla voittoa vaakariveissä jommalla kummalla värillä. Funktio palauttaa 0
    jos voittoa ei ole, 1 jos keltainen voitti ja 2 jos punainen voitti."""
    for y in range(5,2,-1):
            for x in range(6,-1,-1):
                if board[y][x].is_yellow() and board[y-1][x].is_yellow() and board[y-2][x].is_yellow() and board[y-3][x].is_yellow():
                    return 1
                if board[y][x].is_red() and board[y-1][x].is_red() and board[y-2][x].is_red() and board[y-3][x].is_red():
                    return 2
    return 0

def vertical_check(board):
    """Funktio, joka tarkistaa onko pelilaudalla voittoa pystyriveissä jommalla kummalla värillä. Funktio palauttaa 0
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
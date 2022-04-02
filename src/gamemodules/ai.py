"""Moduuli, joka sisältää tekoäly vastuksen logiikkaan liittyviä funktioita"""
from gamemodules import game_logic
def lowest_available(board, x):
    """Funktio, joka etsii halutun sarakkeen x alimman vapaan ruudun koordinaatin y. Jos täynnä niin palauttaa -1"""
    for y in range(5,-1,-1):
        if board[y][x].is_empty():
            return y
    return -1
def calculate_board(board):
    """Funktio, joka palauttaa minimax algoritmille tarvittavan arvosanan kyseisestä pelitilanteesta.
    Arvosana:   +1000 (jos AI voittanut)
                -1000 (jos pelaaja voittanut)
                +10   (AI:lla kolme peräkkäin (ilman että blokattu))
                -100  (Pelaajalla kolme peräkkäin (ilman että blokattu), koska tällöin pelaaja voi voittaa tulevalla vuorollaan)
                +5    (AI:lla kaksi peräkkäin (ilman että blokattu))
                -5    (Pelaajalla kaksi peräkkäin (ilman että blokattu))
    """
    grade = 0
    win = game_logic.win_check(board)
    if win == 1:
        grade += 1000
    elif win == 2:
        grade -= 1000
    else:
        pass
    # kesken...
    return grade
def find_best_move(board):
    bestgrade = -1000
    bestgrade = max(bestgrade, minimax(board, True, 7))

def minimax(board, is_max, depth):
    """Funktio, joka toteuttaa minimax algoritmin. Sille annetaan argumentiksi pelilauta, boolean arvo, joka määrittää ollaanko minimax algoritmin
    min vai max kohdassa. Viimeinen argumentti on syvyys. Kun funktiota ensimmäisen kerran kutsutaan annetaan syyvyys kuinka pitkälle siirtoja halutaan laskea"""
    if depth == 0:
        return calculate_board(board)
    if game_logic.win_check(board) != 0:
        return calculate_board(board)
    if is_max:
        bestgrade = -1000
        for x in range(0,7):
            y = lowest_available(board, x)
            if y == -1:
                continue
            board[y][x].mark_red()
            bestgrade = max(bestgrade, minimax(board, False, depth - 1))
            board[y][x].mark_empty()   
        return bestgrade
    if not is_max:
        bestgrade = 1000
        for x in range(0,7):
            y = lowest_available(board, x)
            if y == -1:
                continue
            board[y][x].mark_yellow()
            bestgrade = min(bestgrade, minimax(board, True, depth - 1))
            board[y][x].mark_empty()
        return bestgrade


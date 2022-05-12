"""Moduuli, joka sisältää tekoäly vastuksen logiikkaan liittyviä funktioita"""
import numpy
from gamemodules import game_logic
ORDER = [3,2,4,1,5,0,6]
INF = 10000000
DEPTH = 5
def lowest_available(board, x):
    """Funktio, joka etsii halutun sarakkeen x alimman vapaan ruudun koordinaatin y. Jos täynnä niin palauttaa -1"""
    for y in range(5,-1,-1):
        if board[y][x].is_empty():
            return y
    return -1
def lowest_available_numbered(numbered_board, x):
    """Funktio, joka etsii numeroidun pelilaudan halutun sarakkeen x alimman vapaan ruudun koordinaatin y. Jos täynnä niin palauttaa -1"""
    for y in range(5,-1,-1):
        if numbered_board[y][x] == 0:
            return y
    return -1
def make_numbered(board):
    numbered = [[0 for x in range(7)] for y in range(6)]
    for y in range(6):
        for x in range(7):
            if board[y][x].is_yellow():
                numbered[y][x] = 1
            if board[y][x].is_red():
                numbered[y][x] = 2
    return numbered
def check_if_4(line):
    if line == [1,1,1,1]:
        return 1
    if line == [2,2,2,2]:
        return 2
    return -1
def count_if_3(line):
    if line == [0,1,1,1] or line == [1,1,1,0]:
        return -100
    if line == [0,2,2,2] or line == [2,2,2,0]:
        return 10
    return 0
def count_if_2(line):
    if line == [0,1,1,0] or line == [0,0,1,1] or line == [1,1,0,0]:
        return -5
    if line == [0,2,2,0] or line == [0,0,2,2] or line == [2,2,0,0]:
        return +5
    return 0
def horisontal_line_check(numbered_board):
    grade_change = 0
    for y in range(5,-1,-1):
        row = numbered_board[y][:]
        for x in range(6,2,-1):
            horisontal = [row[x-3],row[x-2],row[x-1],row[x]]
            # if check_if_4(horisontal) == 2:
            #     return 10000
            # if check_if_4(horisontal) == 1:
            #     return -1000
            grade_change += count_if_3(horisontal)
            grade_change += count_if_2(horisontal)
    return grade_change
def vertical_line_check(numbered_board):
    grade_change = 0
    n_board = numpy.array(numbered_board)
    for x in ORDER:
        col = n_board[:,x]
        for y in range(5,2,-1):
            vertical=[col[y-3],col[y-2],col[y-1],col[y]]
            # if check_if_4(vertical) == 2:
            #     return 10000
            # if check_if_4(vertical) == 1:
            #     return -1000
            grade_change += count_if_3(vertical)
            grade_change += count_if_2(vertical)
    return grade_change
def upwards_diagonal_line_check(numbered_board):
    grade_change = 0
    for y in range(5,2,-1):
        for x in range(3,-1,-1):
            u_diagonal = [numbered_board[y][x],numbered_board[y-1][x+1],
                        numbered_board[y-2][x+2],numbered_board[y-3][x+3]]
            # if check_if_4(u_diagonal) == 2:
            #     return 10000
            # if check_if_4(u_diagonal) == 1:
            #     return -1000
            grade_change += count_if_3(u_diagonal)
            grade_change += count_if_2(u_diagonal)
    return grade_change
def downwards_diagonal_line_check(numbered_board):
    grade_change = 0
    for y in range(5,2,-1):
        for x in range(3,7):
            d_diagonal = [numbered_board[y-3][x-3], numbered_board[y-2][x-2],
                        numbered_board[y-1][x-1], numbered_board[y][x]]
            # if check_if_4(d_diagonal) == 2:
            #     return 10000
            # if check_if_4(d_diagonal) == 1:
            #     return -1000
            grade_change += count_if_3(d_diagonal)
            grade_change += count_if_2(d_diagonal)
    return grade_change
def calculate_board(board):
    """Funktio, joka palauttaa minimax algoritmille tarvittavan arvosanan kyseisestä pelitilanteesta.
    Arvosana:   +10000 (jos AI voittanut)
                -1000 (jos pelaaja voittanut)
                +10   (AI:lla kolme peräkkäin (ilman että blokattu))
                -100  (Pelaajalla kolme peräkkäin (ilman että blokattu), koska tällöin pelaaja voi voittaa tulevalla vuorollaan)
                +5    (AI:lla kaksi peräkkäin (ilman että blokattu))
                -5    (Pelaajalla kaksi peräkkäin (ilman että blokattu))
    """
    grade = 0
    grade += vertical_line_check(board)
    grade += horisontal_line_check(board)
    grade += upwards_diagonal_line_check(board)
    grade += downwards_diagonal_line_check(board)
    return grade

def find_best_move(numbered_board):
    """Funktio, joka palauttaa parhaan reitin. Kutsuu minimax algoritmia."""
    move = (-1, -1)
    bestgrade = -INF
    for x in ORDER:
        y = lowest_available_numbered(numbered_board, x)
        print(y)
        if y == -1:
            continue
        numbered_board[y][x] = 2
        grade = minimax(numbered_board, False, DEPTH, -INF, INF)
        numbered_board[y][x] = 0
        if grade > bestgrade:
            bestgrade = grade
            move =  (y,x)
    return move

def minimax(numbered_board, is_max, depth, alpha, beta):
    """Funktio, joka toteuttaa minimax algoritmin. Sille annetaan argumentiksi pelilauta, boolean arvo, joka määrittää ollaanko minimax algoritmin
    min vai max kohdassa. Viimeinen argumentti on syvyys. Kun funktiota ensimmäisen kerran kutsutaan annetaan syyvyys kuinka pitkälle siirtoja halutaan laskea"""
    if depth == 0:
        return calculate_board(numbered_board)
    winner = game_logic.win_check_numbered(numbered_board)
    if winner == 2:
        return 10000
    if winner == 1:
        return -1000
    if is_max:
        bestgrade = -INF
        for x in ORDER:
            y = lowest_available_numbered(numbered_board, x)
            if y == -1:
                continue
            numbered_board[y][x] = 2
            grade = minimax(numbered_board, False, depth - 1, alpha, beta)
            numbered_board[y][x] = 0
            bestgrade = max(bestgrade, grade)
            alpha = max(alpha, grade)  
            if beta <= alpha:
                break 
        return bestgrade
    if not is_max:
        bestgrade = INF
        for x in ORDER:
            y = lowest_available_numbered(numbered_board, x)
            if y == -1:
                continue
            numbered_board[y][x] = 1
            grade = minimax(numbered_board, True, depth - 1, alpha, beta)
            numbered_board[y][x] = 0
            bestgrade = min(bestgrade, grade)
            beta = min(beta, grade)
            if beta <= alpha:
                break
        return bestgrade


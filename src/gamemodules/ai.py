"""Moduuli, joka sisältää tekoäly vastuksen logiikkaan liittyviä funktioita"""
import numpy
from gamemodules import game_logic
"""ORDER muuttuja on lista x-arvoja, joka kuvaa otollisimman järjestyksen käydä
läpi pelilaudan sarakkeet"""
ORDER = [3,2,4,1,5,0,6]
INF = 10000000
def lowest_available(board, x):
    """Funktio, joka etsii numeroidun pelilaudan halutun sarakkeen x alimman vapaan ruudun koordinaatin y. Jos täynnä niin palauttaa -1"""
    for y in range(5,-1,-1):
        if board[y][x] == 0:
            return y
    return -1
def count_if_4(line):
    """Funktio, joka tarkistaa onko voittoa parametrina saamassaan 4:n listassa
    ja laskee pisteet sen mukaisesti.
    """
    if line == [1,1,1,1]:
        return -1000
    if line == [2,2,2,2]:
        return 10000
    return 0
def count_if_3(line):
    """Funktio, joka antaa parametriksi saamalleen 4:n riville
    oikean arvosanan 3-putkien osalta."""
    if line == [0,1,1,1] or line == [1,1,1,0]:
        return -100
    if line == [0,2,2,2] or line == [2,2,2,0]:
        return 10
    return 0
def horisontal_line_check(board):
    """Funktio, joka tarkistaa arvosanan muutoksen vaakariveiltä."""
    grade_change = 0
    for y in range(5,-1,-1):
        row = board[y][:]
        for x in range(6,2,-1):
            horisontal = [row[x-3],row[x-2],row[x-1],row[x]]
            if count_if_4(horisontal) != 0:
                return count_if_4(horisontal)
            grade_change += count_if_3(horisontal)
    return grade_change
def vertical_line_check(board):
    """Funktio, joka tarkistaa arvosanan muutoksen pystyriveiltä."""
    grade_change = 0
    n_board = numpy.array(board)
    for x in ORDER:
        col = n_board[:,x]
        for y in range(5,2,-1):
            vertical=[col[y-3],col[y-2],col[y-1],col[y]]
            if count_if_4(vertical) != 0:
                return count_if_4(vertical)
            grade_change += count_if_3(vertical)
    return grade_change
def upwards_diagonal_line_check(board):
    """Funktio, joka tarkistaa arvosanan muutoksen ylöspäin viistoon
    olevilta riveiltä (vasemmalta oikealle katsottuna)."""
    grade_change = 0
    for y in range(5,2,-1):
        for x in range(3,-1,-1):
            u_diagonal = [board[y][x],board[y-1][x+1],
                        board[y-2][x+2],board[y-3][x+3]]
            if count_if_4(u_diagonal) != 0:
                return count_if_4(u_diagonal)
            grade_change += count_if_3(u_diagonal)
    return grade_change
def downwards_diagonal_line_check(board):
    """Funktio, joka tarkistaa arvosanan muutoksen alaspäin viistoon
    olevilta riveiltä (vasemmalta oikealle katsottuna)."""
    grade_change = 0
    for y in range(5,2,-1):
        for x in range(3,7):
            d_diagonal = [board[y-3][x-3], board[y-2][x-2],
                        board[y-1][x-1], board[y][x]]
            if count_if_4(d_diagonal) != 0:
                return count_if_4(d_diagonal)
            grade_change += count_if_3(d_diagonal)
    return grade_change
def calculate_board(board):
    """Funktio, joka palauttaa minimax algoritmille tarvittavan
    arvosanan kyseisestä pelitilanteesta.
    Arvosana:   +10000 (jos AI voittanut)
                -1000  (jos pelaaja voittanut)
                +10    (AI:lla mahdollisessa neljän rivissä kolme
                       peräkkäin (ilman että blokattu) eli yhdesta
                       kolmen rivistä voi siis tulla pisteet 2 kertaa
                       jos sen voi täydentää kummastakin päästä.)
                -100   (Pelaajalla mahdollisessa neljän rivissä kolme
                       peräkkäin (ilman että blokattu) eli yhdestä
                       kolmen rivistä voi siis tulla pisteet 2 kertaa,
                       jos sen voi täydentää kummastakin päästä.)
    """
    grade = 0
    grade += vertical_line_check(board)
    if grade >= 10000 or grade <= -1000:
        return grade
    grade += horisontal_line_check(board)
    if grade >= 10000 or grade <= -1000:
        return grade
    grade += upwards_diagonal_line_check(board)
    if grade >= 10000 or grade <= -1000:
        return grade
    grade += downwards_diagonal_line_check(board)
    return grade

def find_best_move(board, depth):
    """Funktio, joka palauttaa parhaan reitin.
    Kutsuu minimax algoritmia."""
    move = (-1, -1)
    bestgrade = -INF
    for x in ORDER:
        y = lowest_available(board, x)
        if y == -1:
            continue
        board[y][x] = 2
        grade = minimax(board, False, depth, -INF, INF)
        board[y][x] = 0
        if grade > bestgrade:
            bestgrade = grade
            move =  (y,x)
    return move

def minimax(board, is_max, depth, alpha, beta):
    """Funktio, joka toteuttaa minimax algoritmin.
    Sille annetaan argumentiksi pelilauta, boolean arvo, 
    joka määrittää ollaanko minimax algoritmin
    min vai max kohdassa. Viimeinen argumentti on syvyys.
    kuinka pitkälle siirtoja halutaan laskea
    (vaikeustason mukaan)"""
    if depth == 0:
        return calculate_board(board)
    winner = game_logic.win_check(board)
    if winner == 2:
        return 10000
    if winner == 1:
        return -1000
    if is_max:
        bestgrade = -INF
        for x in ORDER:
            y = lowest_available(board, x)
            if y == -1:
                continue
            board[y][x] = 2
            grade = minimax(board, False, depth - 1, alpha, beta)
            board[y][x] = 0
            bestgrade = max(bestgrade, grade)
            alpha = max(alpha, grade)  
            if beta <= alpha:
                break 
        return bestgrade
    if not is_max:
        bestgrade = INF
        for x in ORDER:
            y = lowest_available(board, x)
            if y == -1:
                continue
            board[y][x] = 1
            grade = minimax(board, True, depth - 1, alpha, beta)
            board[y][x] = 0
            bestgrade = min(bestgrade, grade)
            beta = min(beta, grade)
            if beta <= alpha:
                break
        return bestgrade


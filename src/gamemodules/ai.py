"""Moduuli, joka sisältää tekoäly vastuksen logiikkaan liittyviä funktioita"""
from gamemodules import game_logic
ORDER = [3,2,4,1,5,0,6]
INF = 10000000
DEPTH = 4
def lowest_available(board, x):
    """Funktio, joka etsii halutun sarakkeen x alimman vapaan ruudun koordinaatin y. Jos täynnä niin palauttaa -1"""
    for y in range(5,-1,-1):
        if board[y][x].is_empty():
            return y
    return -1
def horisontal_line_check(board):
    """Funktio, joka laskee vaakariveillä olevien vierekkäisten 2 ja 3 samaa (blokkaamatonta) aiheuttaman muutoksen pelikentän arvosanaan. Funktio palauttaa tämän arvosanan muutoksen."""
    grade_change = 0
    for y in range(5,-1,-1):
        for x in range(0,5):
            if board[y][x].is_red() and board[y][x+1].is_red() and board[y][x+2].is_red():
                grade_change += 10
            if board[y][x].is_yellow() and board[y][x+1].is_yellow() and board[y][x+2].is_yellow():
                grade_change -= 100
            if x == 0:
                if board[y][x].is_red() and board[y][x+1].is_red() and not board[y][x+2].is_red():
                    grade_change += 5
                if board[y][x].is_yellow() and board[y][x+1].is_yellow() and not board[y][x+2].is_yellow():
                    grade_change -= 5
            if x == 4:
                if not board[y][x].is_red() and board[y][x+1].is_red() and board[y][x+2].is_red():
                    grade_change += 5
                if not board[y][x].is_yellow() and board[y][x+1].is_yellow() and board[y][x+2].is_yellow():
                    grade_change -= 5
            if x != 0:
                if not board[y][x-1].is_red() and board[y][x].is_red() and board[y][x+1].is_red() and board[y][x+2].is_red():
                    grade_change += 5
                if not board[y][x-1].is_yellow() and board[y][x].is_yellow() and board[y][x+1].is_yellow() and board[y][x+2].is_yellow():
                    grade_change -= 5
    return grade_change
def vertical_line_check(board):
    """Funktio, joka laskee pystyriveillä olevien vierekkäisten 2 ja 3 samaa (blokkaamatonta) aiheuttaman muutoksen pelikentän arvosanaan. Funktio palauttaa tämän arvosanan muutoksen."""
    grade_change = 0
    for y in range(5,1,-1):
        for x in range(0,6):
            if board[y][x].is_red() and board[y-1][x].is_red() and board[y-2][x].is_red():
                grade_change += 10
            if board[y][x].is_yellow() and board[y-1][x].is_yellow() and board[y-2][x].is_yellow():
                grade_change -= 100
            if y == 5:
                if board[y][x].is_red() and board[y-1][x].is_red() and not board[y-2][x].is_red():
                    grade_change += 5
                if board[y][x].is_yellow() and board[y-1][x].is_yellow() and not board[y-2][x].is_yellow():
                    grade_change -= 5
            if y == 2:
                if not board[y][x].is_red() and board[y-1][x].is_red() and board[y-2][x].is_red():
                    grade_change += 5
                if not board[y][x].is_yellow() and board[y-1][x].is_yellow() and board[y-2][x].is_yellow():
                    grade_change -= 5
            if y != 5:
                if not board[y+1][x].is_red() and board[y][x].is_red() and board[y-1][x].is_red() and not board[y-2][x].is_red():
                    grade_change += 5
                if not board[y+1][x].is_yellow() and board[y][x].is_yellow() and board[y-1][x].is_yellow() and not board[y-2][x].is_yellow():
                    grade_change -= 5
    return grade_change
def diagonal_upwards_line_check(board):
    """Funktio, joka laskee ylöspäin viistossa olevien vierekkäisten 2 ja 3 samaa (blokkaamatonta) aiheuttaman muutoksen pelikentän arvosanaan. Funktio palauttaa tämän arvosanan muutoksen."""
    grade_change = 0
    for y in range(5,1,-1):
        for x in range(0,5):
            if board[y][x].is_red() and board[y-1][x+1].is_red() and board[y-2][x+2].is_red():
                grade_change += 10
            if board[y][x].is_yellow() and board[y-1][x+1].is_yellow() and board[y-2][x+2].is_yellow():
                grade_change -= 100
            if x == 0 or y == 5:
                if board[y][x].is_red() and board[y-1][x+1].is_red() and not board[y-2][x+2].is_red():
                    grade_change += 5
                if board[y][x].is_yellow() and board[y-1][x+1].is_yellow() and not board[y-2][x+2].is_yellow():
                    grade_change -= 5
            if x == 4 or y == 2:
                if not board[y][x].is_red() and board[y-1][x+1].is_red() and board[y-2][x+2].is_red():
                    grade_change += 5
                if not board[y][x].is_yellow() and board[y-1][x+1].is_yellow() and board[y-2][x+2].is_yellow():
                    grade_change -= 5
            if x != 0 and y != 5:
                if not board[y+1][x-1].is_red() and board[y][x].is_red() and board[y-1][x+1].is_red() and not board[y-2][x+2].is_red():
                    grade_change += 5
                if not board[y+1][x-1].is_yellow() and board[y][x].is_yellow() and board[y-1][x+1].is_yellow() and not board[y-2][x+2].is_yellow():
                    grade_change -= 5
    return grade_change
def diagonal_downwards_line_check(board):
    """Funktio, joka laskee alaspäin viistossa olevien vierekkäisten 2 ja 3 samaa (blokkaamatonta) aiheuttaman muutoksen pelikentän arvosanaan. Funktio palauttaa tämän arvosanan muutoksen."""
    grade_change = 0
    for y in range(5,1,-1):
        for x in range(2,7):
            if board[y][x].is_red() and board[y-1][x-1].is_red() and board[y-2][x-2].is_red():
                grade_change += 10
            if board[y][x].is_yellow() and board[y-1][x-1].is_yellow() and board[y-2][x-2].is_yellow():
                grade_change -= 100
            if x == 6 or y == 5:
                if board[y][x].is_red() and board[y-1][x-1].is_red() and not board[y-2][x-2].is_red():
                    grade_change += 5
                if board[y][x].is_yellow() and board[y-1][x-1].is_yellow() and not board[y-2][x-2].is_yellow():
                    grade_change -= 5
            if x == 2 or y == 2:
                if not board[y][x].is_red() and board[y-1][x-1].is_red() and board[y-2][x-2].is_red():
                    grade_change += 5
                if not board[y][x].is_yellow() and board[y-1][x-1].is_yellow() and board[y-2][x-2].is_yellow():
                    grade_change -= 5
            if y != 5 and x != 6:
                if not board[y+1][x+1].is_red() and board[y][x].is_red() and board[y-1][x-1].is_red() and not board[y-2][x-2].is_red():
                    grade_change += 5
                if not board[y+1][x+1].is_yellow() and board[y][x].is_yellow() and board[y-1][x-1].is_yellow() and not board[y-2][x-2].is_yellow():
                    grade_change -= 5
    return grade_change
def calculate_board(board):
    """Funktio, joka palauttaa minimax algoritmille tarvittavan arvosanan kyseisestä pelitilanteesta.
    Arvosana:   +1000 (jos AI voittanut)
                -1000 (jos pelaaja voittanut)
                +10   (AI:lla kolme peräkkäin (ilman että blokattu))
                -100  (Pelaajalla kolme peräkkäin (ilman että blokattu), koska tällöin pelaaja voi voittaa tulevalla vuorollaan)
                +5    (AI:lla kaksi peräkkäin (ilman että blokattu))
                -5    (Pelaajalla kaksi peräkkäin (ilman että blokattu))
                +2    (jos keskimmäinen sarake alkua varten)
    """
    grade = 0
    win = game_logic.win_check(board)
    if win == 1:
        grade += 1000
    elif win == 2:
        grade -= 1000
    else:
        if board[5][3].is_red():
            grade += 2
        grade += vertical_line_check(board)
        grade += horisontal_line_check(board)
        grade += diagonal_upwards_line_check(board)
        grade += diagonal_downwards_line_check(board)
    return grade

def find_best_move(board):
    """Funktio, joka palauttaa parhaan reitin. Kutsuu minimax algoritmia."""
    move = (-1, -1)
    bestgrade = -INF
    for x in ORDER:
        y = lowest_available(board, x)
        if y == -1:
            continue
        board[y][x].mark_red()
        grade = minimax(board, False, DEPTH, -INF, INF)
        board[y][x].mark_empty()
        if grade > bestgrade:
            bestgrade = grade
            move =  (y,x)
    return move

def minimax(board, is_max, depth, alpha, beta):
    """Funktio, joka toteuttaa minimax algoritmin. Sille annetaan argumentiksi pelilauta, boolean arvo, joka määrittää ollaanko minimax algoritmin
    min vai max kohdassa. Viimeinen argumentti on syvyys. Kun funktiota ensimmäisen kerran kutsutaan annetaan syyvyys kuinka pitkälle siirtoja halutaan laskea"""
    if depth == 0:
        return calculate_board(board)
    if game_logic.win_check(board) != 0:
        return calculate_board(board)
    if is_max:
        bestgrade = -INF
        for x in ORDER:
            y = lowest_available(board, x)
            if y == -1:
                continue
            board[y][x].mark_red()
            grade = minimax(board, False, depth - 1, alpha, beta)
            board[y][x].mark_empty()
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
            board[y][x].mark_yellow()
            grade = minimax(board, True, depth - 1, alpha, beta)
            board[y][x].mark_empty()
            bestgrade = min(bestgrade, grade)
            beta = min(beta, grade)
            if beta <= alpha:
                break
        return bestgrade


from tracemalloc import start
from gamemodules.singleplayer_game import SinglePlayerGame
from gamemodules import ai
from gamemodules import game_logic
import statistics
import random
import time
EASY = 3
HARD = 5
VERY_HARD = 6
def performance_test(game, amount):
    print()
    print("Tässä saattaa kestää hieman...")
    print()
    times = []
    for _ in range(amount):
        board = generate_board()
        game.board = board
        start_time = time.time()
        game.ai_turn()
        end_time = time.time()
        times.append(end_time-start_time) 
    time_mean = statistics.mean(times)
    print(f"Laskettiin tietokonevastuksen siirron miettimiseen kuluva aika {amount} satunnaisessa pelitilanteessa")
    print(f"Suoritusaikojen keskiarvo: {time_mean} sekuntia")
    print()
def generate_board():
    ok = False
    while not ok:
        board = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
        for i in range(11):
            if i % 2 == 0:
                y = -1
                while y == -1:
                    x = random.randint(0,6)
                    y = ai.lowest_available(board, x)
                board[y][x] = 1
            else:
                y = -1
                while y == -1:
                    x = random.randint(0,6)
                    y = ai.lowest_available(board, x)
                board[y][x] = 2
        if game_logic.win_check(board) == 0:
            ok = True
    return board

            
easy_game = SinglePlayerGame(EASY)
hard_game = SinglePlayerGame(HARD)
very_hard_game = SinglePlayerGame(VERY_HARD)
while True:
    level = input("Valitse testattava vaikeustaso (h = helppo, v = vaikea, t = tosi vaikea, l = lopeta):")
    if level == "l":
        break
    print()
    amount = int(input("Otoksen suuruus (Huom. isolla vaikeustasolla iso otos on hidasta arvioida!):"))
    if level == "h":
        performance_test(easy_game, amount)
    if level == "v":
        performance_test(hard_game, amount)
    if level == "t":
        performance_test(very_hard_game, amount)


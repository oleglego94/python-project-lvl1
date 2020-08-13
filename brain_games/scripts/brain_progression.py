#!/usr/bin/env python3
"""Run script for game: arithmetical progression """


from brain_games.games import progression_logic
from brain_games import game_engine


def main():
    start_msg = 'What number is missing in the progression?\n'
    game_engine.play_game(start_msg, progression_logic.generate_qa)


if __name__ == '__main__':
    main()

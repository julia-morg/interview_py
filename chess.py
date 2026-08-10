#!/usr/bin/env python3
import sys

from src.board import Board


def main():
    try:
        board = Board()
        for move in sys.argv[1:]:
            board.move(move)
        board.dump()
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()

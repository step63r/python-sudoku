import argparse
import numpy as np


from pathlib import Path
import time


from Sudoku import Sudoku


def dfs(board, res):
    """
    Solve Sudoku with DFS (backtracking)

    Parameters
    ----------
    board : Sudoku
        Sudoku board to be solved
    res : list<numpy.ndarray>
        Solved boards

    Returns
    -------
    list<Sudoku>
        All solved Sudoku boards
    """
    x, y = board.find_empty()

    if x == y == -1:
        res.append(board.get())
        return
    
    for value in board.find_choices(x, y):
        board.put(x, y, value)
        dfs(board, res)
        board.reset(x, y)


def format_board(board):
    """
    Format ndarray like Sudoku

    Parameters
    ----------
    board : numpy.ndarray
        Sudoku board

    Returns
    -------
    str
        Formatted string
    """
    ret = ""
    ret += "-------------------------\n"
    for x in range(0, 9):
        ret += "| "
        for y in range(0, 9):
            ret += f"{board[x][y]} "
            if y % 3 == 2:
                ret += "| "
        ret += "\n"
        if x % 3 == 2:
            ret += "-------------------------\n"
    return ret


def main(args):
    """
    Main method

    Parameters
    ----------
    args : obj
        Command line arguments
    """
    src = args.src

    with open(src, "r") as f:
        src_data = [s.strip() for s in f.readlines()]

    board = Sudoku()
    for x in range(0, 9):
        for y in range(0, 9):
            if src_data[x][y] == "*":
                continue
            board.put(x, y, int(src_data[x][y]))
    
    results = []
    start_time = time.time()
    dfs(board, results)
    end_time = time.time()
    print(f"{len(results)} results, {end_time - start_time:.4f} sec")

    if not results:
        print("No solutions.")

    else:
        i = 1
        for result in results:
            print(f"No.{i}")
            print(format_board(result))
            i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Sudoku (number place) with DFS (backtracking)")
    parser.add_argument("src", help="Source file path")
    args = parser.parse_args()
    main(args)

import argparse
import copy
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
    # Keep Sudoku board status
    board_prev = copy.deepcopy(board)

    # Fill cells uniquely determined
    board.process()

    x, y = board.find_empty()

    if x == y == -1:
        res.append(board.get())
        # Undo before return
        board = copy.deepcopy(board_prev)
        return

    for value in board.find_choices(x, y):
        board.put(x, y, value)
        dfs(board, res)
        board.reset(x, y)
        # For Python recursive call method
        board = copy.deepcopy(board_prev)
    
    # Undo
    board = copy.deepcopy(board_prev)


def format_print(board):
    """
    Print formatted sudoku board
    """
    print("    0 1 2   3 4 5   6 7 8  ")
    print("  -------------------------")
    for x in range(0, 9):
        print(f"{x} | ", end="")
        for y in range(0, 9):
            if board[x][y] == -1:
                print("* ", end="")
            else:
                print(f"{board[x][y]} ", end="")
            if y % 3 == 2:
                print("| ", end="")
        print("")
        if x % 3 == 2:
            print("  -------------------------")


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
    pattern = args.pattern
    src_path = Path(src)

    if not src_path.exists():
        raise FileNotFoundError("Path \"src\" is not a file or directory")

    file_list = []
    if src_path.is_dir():
        file_list = list(src_path.glob(pattern))

    elif src_path.is_file():
        file_list = [src_path]

    elapsed_time = 0.0
    for one_src_path in file_list:
        with open(one_src_path, "r") as f:
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
        elapsed_time += end_time - start_time
        print(f"File: {one_src_path.name}")
        print(f"{len(results)} results, {end_time - start_time:.4f} sec")

        if not results:
            print("No solutions.")

        else:
            i = 1
            for result in results:
                print(f"No.{i}")
                print(format_board(result))
                i += 1
    
    print("--------------------------------------------------")
    print("Complete!!")
    print("--------------------------------------------------")
    print(f"Elapsed Time: {elapsed_time:.4f} sec")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Sudoku (number place) with DFS (backtracking)")
    parser.add_argument("src", help="Source file path")
    parser.add_argument("-p", "--pattern", default="*.txt", help="Source filename pattern (by default \"*.txt\")")
    args = parser.parse_args()
    main(args)

import numpy as np


class Sudoku:
    """
    Sudoku model class
    """
    # Numpy field (-1 as undefined cell value)
    field = np.full((9, 9), -1)

    def __init__(self):
        """
        Constructor
        """
        pass
    
    def get(self):
        """
        Get current numpy field

        Returns
        -------
        numpy.ndarray
            Numpy field
        """
        return self.field.copy()
    
    def find_empty(self):
        """
        Get first empty cell from left top

        Returns
        -------
        (int, int)
            Index of empty cell (if not found return (-1, -1))
        """
        for x in range(0, 9):
            for y in range(0, 9):
                if self.field[x][y] == -1:
                    return (x, y)
        return (-1, -1)

    def find_choices(self, x, y):
        """
        Get available choices at the cell

        Parameters
        ----------
        x : int
            Row index
        y : int
            Column index

        Returns
        -------
        list<int>
            Available choices at (x, y)
        """
        can_use = {i + 1 for i in range(0, 9)}

        # Horizontal check
        for i in range(0, 9):
            if self.field[x][i] != -1:
                can_use.discard(self.field[x][i])
        
        # Vertical check
        for i in range(0, 9):
            if self.field[i][y] != -1:
                can_use.discard(self.field[i][y])
        
        # Box check
        cx = int(int(x / 3) * 3) + 1
        cy = int(int(y / 3) * 3) + 1
        for i in range(cx - 1, cx + 2):
            for j in range(cy - 1, cy + 2):
                if self.field[i][j] != -1:
                    can_use.discard(self.field[i][j])
        
        return can_use
    
    def put(self, x, y, value):
        """
        Put value

        Parameters
        ----------
        x : int
            Row index
        y : int
            Column index
        value : int
            Detected cell value
        """
        self.field[x][y] = value

    def reset(self, x, y):
        """
        Reset value to -1

        Parameters
        ----------
        x : int
            Row index
        y : int
            Column index
        """
        self.field[x][y] = -1

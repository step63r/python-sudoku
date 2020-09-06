import numpy as np

# 盤面を二次元ベクトルで表す
ALL_NUMBERS = {1, 2, 3, 4, 5, 6, 7, 8, 9}

class Sudoku:
    """
    Sudoku model class
    """
    # Sudoku field
    field = np.array([[]])

    # nums[x][y][v] ← number of v+1 value in row, column and block containing (x, y)
    nums = np.array([[[]]])

    # choices[x][y] ← choices can be fill (x, y)
    choices = np.array([[]])

    def __init__(self):
        """
        Constructor
        """
        self.field = np.full((9, 9), -1)
        self.nums = np.full((9, 9, 9), 0)
        self.choices = np.full((9, 9), set())
        for x in range(0, 9):
            for y in range(0, 9):
                self.choices[x][y] = ALL_NUMBERS.copy()
    
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
        Get cell with the fewest choices in empty cells

        Returns
        -------
        (int, int)
            Index of empty cell (if not found return (-1, -1))
        """
        min_num_choices = 10
        ret_x, ret_y = (-1, -1)

        for x in range(0, 9):
            for y in range(0, 9):
                if self.field[x][y] != -1:
                    continue

                if (min_num_choices > len(self.choices[x][y])):
                    min_num_choices = len(self.choices[x][y])
                    ret_x = x
                    ret_y = y

        return (ret_x, ret_y)

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
        set<int>
            Available choices at (x, y)
        """
        return self.choices[x][y].copy()
    
    def print(self):
        """
        Print formatted sudoku board
        """
        print("    0 1 2   3 4 5   6 7 8  ")
        print("  -------------------------")
        for x in range(0, 9):
            print(f"{x} | ", end="")
            for y in range(0, 9):
                if self.field[x][y] == -1:
                    print("* ", end="")
                else:
                    print(f"{self.field[x][y]} ", end="")
                if y % 3 == 2:
                    print("| ", end="")
            print("")
            if x % 3 == 2:
                print("  -------------------------")

    def put_detail(self, x, y, val, x2, y2):
        """
        Impact to (x2, y2) on putting val in (x, y)

        Parameters
        ----------
        x : int
            Source row index
        y : int
            Source column index
        value : int
            Value
        x2 : int
            Target row index
        y2 : int
            Target column index
        """
        if x == x2 and y == y2:
            return
        
        # Nothing to do if (x2, y2) has already value
        if self.field[x2][y2] != -1:
            return
        
        # Remove from choice if there are no val at impact range of (x2, y2)
        if self.nums[x2][y2][val - 1] == 0:
            self.choices[x2][y2].discard(val)
        
        # Update nums
        self.nums[x2][y2][val - 1] += 1

    def put(self, x, y, val):
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
        # Put value
        self.field[x][y] = val

        # Update impact to row, column and block containing (x, y)
        for i in range(0, 9):
            self.put_detail(x, y, val, x, i)
        
        for i in range(0, 9):
            self.put_detail(x, y, val, i, y)
        
        cx = int(int(x / 3) * 3) + 1
        cy = int(int(y / 3) * 3) + 1
        for i in range(cx - 1, cx + 2):
            for j in range(cy - 1, cy + 2):
                self.put_detail(x, y, val, i, j)
    
    def reset_detail(self, x, y, val, x2, y2):
        """
        Impact to (x2, y2) on removing val from (x, y)

        Parameters
        ----------
        x : int
            Source row index
        y : int
            Source column index
        value : int
            Value
        x2 : int
            Target row index
        y2 : int
            Target column index
        """
        if x == x2 and y == y2:
            return

        # Nothing to do if (x2, y2) has already value
        if self.field[x2][y2] != -1:
            return
        
        # Update nums
        self.nums[x2][y2][val - 1] -= 1

        # Regenerate val to choice if nums gets 0
        if self.nums[x2][y2][val - 1] == 0:
            self.choices[x2][y2].add(val)

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
        # Update impact to row, column and block containing (x, y)
        val = self.field[x][y]

        for i in range(0, 9):
            self.reset_detail(x, y, val, x, i)
        
        for i in range(0, 9):
            self.reset_detail(x, y, val, i, y)

        cx = int(int(x / 3) * 3) + 1
        cy = int(int(y / 3) * 3) + 1
        for i in range(cx - 1, cx + 2):
            for j in range(cy - 1, cy + 2):
                self.reset_detail(x, y, val, i, j)
        
        # Remove value
        self.field[x][y] = -1

    def process(self):
        """
        Fill cells uniquely determined
        """
        # Process value 1, 2, ..., 9 in order
        for val in range(1, 10):
            # For each row
            for x in range(0, 9):
                exist = False
                can_enter = []
                for y in range(0, 9):
                    if self.field[x][y] == val:
                        exist = True
                    if self.field[x][y] == -1 and val in self.choices[x][y]:
                        can_enter.append(y)

                # Put val if only one cell can do
                if not exist and len(can_enter) == 1:
                    y = can_enter[0]
                    self.put(x, y, val)
                
            # For each column
            for y in range(0, 9):
                exist = False
                can_enter = []
                for x in range(0, 9):
                    if self.field[x][y] == val:
                        exist = True
                    if self.field[x][y] == -1 and val in self.choices[x][y]:
                        can_enter.append(x)

                # Put val in only one cell can do
                if not exist and len(can_enter) == 1:
                    x = can_enter[0]
                    self.put(x, y, val)
            
            # For each block
            for bx in range(0, 3):
                for by in range(0, 3):
                    exist = False
                    can_enter = []
                    for x in range(bx * 3, (bx + 1) * 3):
                        for y in range(by * 3, (by + 1) * 3):
                            if self.field[x][y] == val:
                                exist = True
                            if self.field[x][y] == -1 and val in self.choices[x][y]:
                                can_enter.append((x, y))
                    
                    # Put val if only one cell can do
                    if not exist and len(can_enter) == 1:
                        x = can_enter[0][0]
                        y = can_enter[0][1]
                        self.put(x, y, val)

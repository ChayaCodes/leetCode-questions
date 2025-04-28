class Solution:
    def is_alive(self, value):
        """
        Checks if the cell is alive. 1 and 3 are considered alive (3 is a transitioning cell to dead).
        """
        return value in [1, 3]

    def count_live_neighbors(self, board, row, col):
        """
        Counts the number of live neighbors for a given cell on the board.
        """
        live_neighbors = 0
        # Directions for the 8 neighboring cells
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for direction in directions:
            neighbor_row = row + direction[0]
            neighbor_col = col + direction[1]
            # Check boundaries to avoid errors
            if 0 <= neighbor_row < len(board) and 0 <= neighbor_col < len(board[0]) and self.is_alive(board[neighbor_row][neighbor_col]):
                live_neighbors += 1
        return live_neighbors

    def apply_rules(self, board, row, col):
        """
        Applies the Game of Life rules to a given cell and updates the board accordingly.
        """
        live_neighbors = self.count_live_neighbors(board, row, col)
        if self.is_alive(board[row][col]):
            if live_neighbors < 2 or live_neighbors > 3:
                # Live cell dies
                board[row][col] = 3
        else:
            if live_neighbors == 3:
                # Dead cell becomes alive
                board[row][col] = 2

    def update_board(self, board):
        """
        Updates the board to the next state based on the transition states.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 2:
                    board[row][col] = 1  # Dead to alive
                elif board[row][col] == 3:
                    board[row][col] = 0  # Alive to dead

    def gameOfLife(self, board):
        """
        Updates the board according to the rules of Conway's Game of Life.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.apply_rules(board, row, col)
        
        self.update_board(board)


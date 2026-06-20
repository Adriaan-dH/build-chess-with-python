"""File 5: Click handling and game state.

Game stores turn, selection, valid moves, and status. Board handles rules;
renderer.py draws the resulting state. Initial clicks only produce logs.
"""

from board import Board
from piece import WHITE


class Game:
    """Keep the state that belongs to one game of chess."""

    def __init__(self):
        """Create a fresh board and the variables the UI will inspect.

        `selected` is None or a `(row, col)` tuple. `valid_moves` starts empty.
        """
        self.board = Board()
        self.turn = WHITE
        self.selected = None
        self.valid_moves = []
        self.status = "Starter board running: terminal logging enabled."

    def handle_square_click(self, square):
        """Respond to a click on one board square and return a debug message.

        TODO 2: When the clicked square contains a piece whose color is
        `self.turn`, store the square in `self.selected` and its moves in
        `self.valid_moves`; otherwise clear both. TODO 5: When a selected
        square is clicked again and is in `self.valid_moves`, call `move_piece`.

        TODO 2 example: when White clicks its pawn on e2 `(6, 4)`, set
        `self.selected = (6, 4)` and set `self.valid_moves` to the board's
        results. A click on a black piece or an empty square clears selection.

        TODO 5 example: with e2 selected, a click on e4 `(4, 4)` is valid if
        it appears in `self.valid_moves`. Move it, change `self.turn` with
        `opponent(self.turn)`, then clear the selection and move markers.
        """
        row, col = square
        piece = self.board.piece_at(row, col)
        if piece is None:
            self.status = f"Empty square: row {row}, column {col}."
            return "No piece selected: square is empty."

        self.status = f"Clicked {piece}. Selection comes in TODO 2."
        return f"Clicked {piece}; selection is not implemented yet."

    def reset(self):
        """Start a new game when the player presses R.

        TODO 5: Reset the board, turn, selection, move markers, and status
        together. The existing `self.__init__()` call already does this.

        Hint: this method already calls `self.__init__()`, which makes
        a new board and restores White's turn, no selection, and no markers.
        """
        self.__init__()

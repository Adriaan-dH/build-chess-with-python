"""File 2: Chess piece data.

This module stores piece colour and type. Movement rules belong in board.py;
drawing belongs in renderer.py.
"""

# These names avoid fragile "magic strings" scattered through the rest of the
# program.  Prefer writing WHITE over writing "white" by hand everywhere.
WHITE = "white"
BLACK = "black"

PAWN = "pawn"
KNIGHT = "knight"
BISHOP = "bishop"
ROOK = "rook"
QUEEN = "queen"
KING = "king"


class Piece:
    """Store the smallest useful description of one chess piece.

    TODO 8: In `__init__`, store `self.has_moved = False`; set it to True
    after a successful move so pawn-first-move and castling rules can inspect it.

    Hint: in `__init__`, add `self.has_moved = False`. After
    `move_piece` moves that object, set it to True. This is needed for a
    pawn's two-square first move and castling (the king and rook must both
    still have False).
    """

    def __init__(self, color, kind):
        """Create a piece, for example `Piece(WHITE, PAWN)`.

        `self` means this specific Piece object. The assignments store its data.
        """
        self.color = color
        self.kind = kind

    def __repr__(self):
        """Return text for console output and debug logs."""
        return f"{self.color} {self.kind}"


def opponent(color):
    """Return the other colour. Use after a successful move to switch turns."""
    if color == WHITE:
        return BLACK
    return WHITE

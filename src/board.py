"""File 3: Board state and chess rules.

Board stores square contents only. Mouse input belongs in game.py; drawing
belongs in renderer.py. Rows run top-to-bottom (0 to 7); columns run left-to-
right (0 to 7). `(7, 0)` is a1 and `(0, 7)` is h8.
"""

from piece import BISHOP, BLACK, KING, KNIGHT, PAWN, QUEEN, ROOK, WHITE, Piece

# These values are shared with the renderer so the window and board agree on
# their dimensions.  Eight columns in a 640-pixel board means 80-pixel squares.
WIDTH = HEIGHT = 640
ROWS = COLS = 8
SQUARE_SIZE = WIDTH // COLS


class Board:
    """A two-dimensional list of Piece objects, or None for an empty square."""

    def __init__(self):
        """Create an empty 8 by 8 grid, then offer a place for the pieces.

        `None` means the square is empty.
        """
        self.squares = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.setup_starting_position()

    def setup_starting_position(self):
        """Put chess pieces into their opening positions.

        TODO 1: Call `place_piece` to populate all 32 opening pieces:
        white pawns on row 6, black pawns on row 1, then each back row. Start
        with the one-line example below; it puts a white pawn on a2.

        Example for a single white pawn on a2:
            self.place_piece(6, 0, Piece(WHITE, PAWN))

        Hint: add all white pawns (row 6, columns 0-7),
        then black pawns (row 1), then the back rows:
            # White back row (row 7): rook, knight, bishop, queen, king, bishop, knight, rook
            self.place_piece(7, 0, Piece(WHITE, ROOK))
            self.place_piece(7, 1, Piece(WHITE, KNIGHT))
            # ... continue for rest of pieces
            # Black back row (row 0): same as above but with BLACK
            self.place_piece(0, 0, Piece(BLACK, ROOK))

        Coordinates:
        - White pawns start on row 6; black pawns start on row 1.
        - White's back row is 7; black's back row is 0.
        - A back row is rook, knight, bishop, queen, king, bishop, knight, rook.
        """
        # Initial checkpoint: empty board. Add `self.place_piece(...)` calls here.
        pass

    @staticmethod
    def in_bounds(row, col):
        """Return True only when a row and column are valid board coordinates.

        TODO 4: Before looking up a candidate move in `self.squares`, call
        this method and skip that move when it returns False. For
        example, `in_bounds(5, 4)` is True but `in_bounds(8, 4)` is False;
        never read `self.squares[8][4]`.
        """
        return 0 <= row < ROWS and 0 <= col < COLS

    def piece_at(self, row, col):
        """Return the piece at one square, or None when the square is empty.

        Used by click handling and move validation.
        """
        return self.squares[row][col]

    def place_piece(self, row, col, piece):
        """Place a Piece object on a square without checking chess rules.

        Overwrites any existing piece. Use for setup and small test positions,
        not for normal player moves.
        """
        self.squares[row][col] = piece

    def move_piece(self, start, end):
        """Move a piece from `start` to `end` after legality is confirmed.

        TODO 3: Move a valid piece, clear the old square, and return True.
        Reject invalid coordinates or an empty start with False. `start` and
        `end` are tuples such as `(6, 4)` and `(4, 4)`.

        Hint:
        1. Check both coordinates with `in_bounds(*start)` and `in_bounds(*end)`.
        2. Get the piece at `start`; if it is None, return False.
        3. Assign it to `end`, then assign None to `start`.
        4. Return True. For example, moving e2 `(6, 4)` to e4 `(4, 4)`
           leaves `(6, 4)` empty.
        """
        # Safe placeholder until basic movement is implemented.
        return False

    def moves_for_piece(self, row, col):
        """Return a list of destinations that a selected piece may move to.

        TODO 4: If the piece is a pawn, build and return its legal forward
        and capture destinations. Return destinations such as `[(5, 4), (4, 4)]`;
        renderer.py draws a marker for every result. Add other types separately.

        Pawn example: a white pawn on e2 `(6, 4)` moves "up" to `(5, 4)` if
        empty. On its first move it may also go to `(4, 4)` when both squares
        are empty. It captures an enemy only at `(5, 3)` or `(5, 5)`.

        TODO 6: Add the remaining piece types after pawns:
        - Rook on a1 `(7, 0)`: scan left, right, up, and down until a piece blocks.
        - Bishop on d5 `(3, 3)`: scan the four diagonal directions until blocked.
        - Knight on b1 `(7, 1)`: try L-shaped offsets like `(-2, -1)`; it jumps pieces.
        - Queen: combine the rook and bishop directions.
        - King: try each adjacent square, such as `(-1, 0)` and `(1, 1)`.
        """
        return []

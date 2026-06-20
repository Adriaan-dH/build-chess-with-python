"""File 4: Pygame drawing.

This module draws Board/Game state and contains no move-validation rules.
"""

import pygame

from board import COLS, HEIGHT, ROWS, SQUARE_SIZE, WIDTH

# A little extra height gives us a friendly status panel below the board.
WINDOW_HEIGHT = HEIGHT + 96

LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)
SELECTED_SQUARE = (246, 246, 105)
MOVE_MARKER = (55, 100, 60)
PANEL = (35, 37, 42)
TEXT = (245, 245, 245)
MUTED_TEXT = (185, 190, 198)

# Note: no drawing change is required for the starter: use this mapping
# to render pieces as Unicode. Later, replace this dictionary with PNG loading
# from assests/pieces.
PIECE_GLYPHS = {
    ("white", "pawn"): "♙", ("white", "knight"): "♘", ("white", "bishop"): "♗",
    ("white", "rook"): "♖", ("white", "queen"): "♕", ("white", "king"): "♔",
    ("black", "pawn"): "♟", ("black", "knight"): "♞", ("black", "bishop"): "♝",
    ("black", "rook"): "♜", ("black", "queen"): "♛", ("black", "king"): "♚",
}


class Renderer:
    """Turn the game's data into pixels on the Pygame window."""

    def __init__(self):
        """Create the fonts once instead of recreating them every frame.

        Fonts are created once because `draw` runs about 60 times per second.
        """
        self.font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 21)
        self.piece_font = pygame.font.SysFont("DejaVu Sans", 64)

    def square_from_mouse(self, position):
        """Convert mouse pixels like (130, 250) into a board square like (3, 1).

        Return None for a click on the status panel. Row comes from y; column
        comes from x.
        """
        x, y = position
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            return y // SQUARE_SIZE, x // SQUARE_SIZE
        return None

    def draw(self, window, game):
        """Draw one complete frame in a predictable back-to-front order.

        Draw order: squares, pieces, then panel.
        """
        self._draw_squares(window, game)
        self._draw_pieces(window, game.board)
        self._draw_status(window, game)

    def _draw_squares(self, window, game):
        """Paint all 64 alternating board squares and optional move markers.

        Note: no renderer change is required. In game.py, set
        `game.selected` to the clicked friendly square and `game.valid_moves`
        to its destinations; this loop already draws the border and markers.
        For example, e2 `(6, 4)` is bordered and `(5, 4)` gets a green marker.
        """
        for row in range(ROWS):
            for col in range(COLS):
                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
                rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(window, color, rect)

                if (row, col) == game.selected:
                    pygame.draw.rect(window, SELECTED_SQUARE, rect, 5)
                if (row, col) in game.valid_moves:
                    pygame.draw.circle(window, MOVE_MARKER, rect.center, 10)

                # Labels appear along the left and bottom edges only.
                if row == ROWS - 1:
                    label = self.small_font.render(chr(ord("a") + col), True, DARK_SQUARE if color == LIGHT_SQUARE else LIGHT_SQUARE)
                    window.blit(label, (rect.right - 15, rect.bottom - 21))
                if col == 0:
                    label = self.small_font.render(str(8 - row), True, DARK_SQUARE if color == LIGHT_SQUARE else LIGHT_SQUARE)
                    window.blit(label, (rect.x + 5, rect.y + 3))

    def _draw_pieces(self, window, board):
        """Draw every non-empty square using its colour and kind.

        Works once Board contains pieces.
        """
        for row in range(ROWS):
            for col in range(COLS):
                piece = board.piece_at(row, col)
                if piece is None:
                    continue

                glyph = PIECE_GLYPHS[(piece.color, piece.kind)]
                fill = (249, 248, 240) if piece.color == "white" else (38, 38, 42)
                outline = (45, 39, 34) if piece.color == "white" else (235, 216, 181)
                image = self.piece_font.render(glyph, True, fill)
                border = self.piece_font.render(glyph, True, outline)
                x = col * SQUARE_SIZE + (SQUARE_SIZE - image.get_width()) // 2
                y = row * SQUARE_SIZE + (SQUARE_SIZE - image.get_height()) // 2 - 4

                # Four border copies create a thin contrast outline.
                for x_offset, y_offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    window.blit(border, (x + x_offset, y + y_offset))
                window.blit(image, (x, y))

    def _draw_status(self, window, game):
        """Draw a short human-readable status message below the chessboard.

        TODO 5: In game.py, set `game.status` after every selection and
        completed move; this method already displays it. For example, use
        "White selected e2" or "Black to move".
        """
        panel = pygame.Rect(0, HEIGHT, WIDTH, WINDOW_HEIGHT - HEIGHT)
        pygame.draw.rect(window, PANEL, panel)
        status = self.font.render(game.status, True, TEXT)
        hint = self.small_font.render("Click the board and read the terminal logs. R resets the game.", True, MUTED_TEXT)
        window.blit(status, (16, HEIGHT + 14))
        window.blit(hint, (16, HEIGHT + 52))

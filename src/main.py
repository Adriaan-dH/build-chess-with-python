"""File 1: Program entry point and Pygame loop.

Run with `make run`. This module connects input, Game, Renderer, and terminal
logs. Chess rules belong in board.py and game.py.
"""

import pygame

from board import WIDTH
from game import Game
from renderer import Renderer, WINDOW_HEIGHT


def main():
    """Create the window, process input, and draw frames until the user quits.

    Each loop handles queued events, draws the latest state, and limits frame
    rate to avoid unnecessary CPU use.
    """
    pygame.init()  # Required before creating a Pygame window or font.
    window = pygame.display.set_mode((WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Chess But Worse")
    clock = pygame.time.Clock()

    game = Game()  # Stores chess state; does not draw.
    renderer = Renderer()  # Draws current state; does not validate rules.
    debug_log("Application started.")

    running = True
    while running:
        # pygame.event.get() reads and clears queued input events.
        for event in pygame.event.get():
            close_events = (pygame.QUIT, pygame.WINDOWCLOSE)
            if event.type in close_events:
                debug_log("Close event received. Shutting down cleanly.")
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Convert click pixels to a board square; None means the panel.
                square = renderer.square_from_mouse(event.pos)
                debug_log(f"Left click: pixels={event.pos}, square={square_label(square)}")
                if square is not None:
                    debug_log(f"Game response: {game.handle_square_click(square)}")

            if event.type == pygame.KEYDOWN:
                debug_log(f"Key pressed: {pygame.key.name(event.key)}")
                if event.key == pygame.K_r:
                    game.reset()
                    debug_log("Game reset to its current starting-position setup.")

        # Draw after input so state changes appear in the same frame.
        renderer.draw(window, game)
        pygame.display.flip()  # Show the completed frame.
        clock.tick(60)  # Aim for at most 60 frames per second.


# ---------------------------------------------------------------------------
# BEGINNER DEBUG LOGGING
# Keep this block near the bottom. Every click, key press, reset, and later move
# should produce a useful line here. Add temporary debug_log calls as needed.
# ---------------------------------------------------------------------------
def debug_log(message):
    """Print one labelled message to the terminal running `make run`."""
    print(f"[CHESS DEBUG] {message}")


def square_label(square):
    """Turn `(row, col)` into friendly chess notation such as `e2` for logs."""
    if square is None:
        return "outside the board"
    row, col = square
    return f"{chr(ord('a') + col)}{8 - row}"


if __name__ == "__main__":
    # This guard lets this file run normally but avoids starting a window if a
    # future test imports `main` only to use one of its helper functions.
    main()

# Learn Python Though Creating Your Own Chess Game

### By Adriaan den Haan

This is a beginner-friendly guided project for learning Python by building a chess game and its logic from scratch. Linux is recommended for the smoothest setup experience, and the included Makefile is used to make running the project as easy as possible. Running `make run` with the code as-is will open the chess board and show the debug terminal, along with some basic starter functionality, to help beginners kick-start the project before working through the TODOs, hints, and step-by-step implementation tasks.

## 0. Setup

```bash
make setup
```

to run the code, simply run:

```bash
make run
```

Expected result: an empty labelled board and `[CHESS DEBUG]` messages in the
terminal for every click, key press, reset, and close event.

## File map

```text
main.py     Pygame loop, input, and terminal logs
game.py     Turn, selection, status, and click handling
board.py    Piece positions and chess rules
piece.py    Piece colour and type
renderer.py Drawing only
```

## Read these files first

These five file numbers are not coding tasks. Read the files in this order
before starting TODO 1; each file introduces the next one.

### File 1: `src/main.py`: the runnable application

The file numbers are only a temporary reading guide. They show the intended
order for understanding the starter, not an order built into the program. You
can remove them later once everyone knows where each responsibility lives.

Read `src/main.py` first. Find:

- Pygame setup;
- the `while running` game loop;
- mouse and keyboard events;
- the debug block near the bottom.

Press `R` and confirm the reset log appears. Close the window with X and
confirm the close log appears.

### File 2: `src/piece.py`: what a piece stores

Read `src/piece.py`.

```python
pawn = Piece(WHITE, PAWN)
```

Keep movement rules out of this file. `Piece` stores only a piece's colour and
kind; its `has_moved` field is added later for castling and a pawn's first move.

### File 3: `src/board.py`: board state and movement rules

Read `src/board.py`. Notice that `Board` stores pieces and will own chess rules.

### File 4: `src/renderer.py`: drawing only

Read `src/renderer.py`. It reads board and game state to draw the window; it
does not decide whether a move is legal.

### File 5: `src/game.py`: turns and click handling

Read `src/game.py`. `Game` connects clicks to `Board`, remembers whose turn it
is, and provides the selection and status values used by the renderer.

Your first code TODO is **TODO 1**: `Board.setup_starting_position` in
`src/board.py`. Everything above is preparation only.

## Implementation TODO index

Work from this list in order. Each TODO in the source repeats its TODO number
and includes local hints and examples.

### TODO 1: Opening position: `src/board.py`

Implement `Board.setup_starting_position`. Add all white and black pawns, then
both back ranks. Start with the white pawn example in that method. White starts
on rows 6 and 7; black starts on rows 1 and 0.

### TODO 2: Selection: `src/game.py`

Implement the first half of `Game.handle_square_click`: select a piece only
when it matches `self.turn`, store its square and valid moves, and clear the
selection for empty squares or enemy pieces.

### TODO 3: Move board data: `src/board.py`

Implement `Board.move_piece(start, end)`. Reject invalid coordinates and empty
starts; otherwise move the piece, clear its old square, and return `True`.

### TODO 4: Pawn destinations: `src/board.py`

Implement pawn moves in `Board.moves_for_piece`: one or two forward squares
when empty, plus diagonal captures of enemies. Check bounds before reading a
candidate square.

### TODO 5: Connect moves to clicks: `src/game.py`

Finish `Game.handle_square_click`: make a valid selected move, clear selection
and markers, switch turns, and update the status message.

### TODO 6: Other pieces: `src/board.py`

Add knight, rook, bishop, queen, and king destinations to
`Board.moves_for_piece`. Friendly pieces block movement; enemies may be the
final destination, but movement never continues through them.

### TODO 7: Check and game end: `src/board.py`, `src/game.py`

Add king lookup, attacked-square checks, check display, rejection of moves that
leave a king in check, then checkmate and stalemate detection.

### TODO 8: Special moves: `src/board.py`, `src/game.py`, `src/piece.py`

Add castling, en passant, and promotion. Optional extensions are the fifty-move
rule and threefold repetition. Use `place_piece` to make small test positions.


## Before a commit

Only commit a feature after it launches, closes cleanly, and has been tested.

### Contact
Adriaan den Haan
adenhaan1@gmail.com

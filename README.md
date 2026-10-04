# Guess The Number

A terminal Number Guessing Game, built as the day 12 project of Udemy's
*100 Days of Code™: The Complete Python Pro Bootcamp*.

The computer picks a number between 1 and 100. Choose a difficulty and guess it:

| Level | Attempts |
|-------|----------|
| easy  | 10       |
| hard  | 5        |

After each guess you are told whether it was too high or too low.

## Requirements

- Python 3.13 or newer
- No runtime dependencies (`pytest` is only needed for the tests)

## Setup

Create and activate a local virtual environment, then upgrade pip.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Linux / macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## Run the game

```bash
python -m pip install -e .
python -m guess_the_number
```

## Run the tests

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

## Documentation

Source comments use Doxygen. With [Doxygen](https://www.doxygen.nl/) installed:

```bash
doxygen docs/Doxyfile
```

The HTML output is written to `docs/build/html`.

## Project layout

```
src/guess_the_number/   game code (constants.py, game.py)
tests/                  pytest tests
docs/                   Doxyfile
```

The functions `set_difficulty`, `check_answer` and `play_game` follow the
course assignment's naming.

## License

See [LICENSE](LICENSE).

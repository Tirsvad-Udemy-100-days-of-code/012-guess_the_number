import pytest

from guess_the_number import game
from guess_the_number.constants import EASY_ATTEMPTS, HARD_ATTEMPTS


def test_set_difficulty():
    assert game.set_difficulty("easy") == EASY_ATTEMPTS
    assert game.set_difficulty(" HARD ") == HARD_ATTEMPTS


def test_set_difficulty_invalid():
    with pytest.raises(ValueError):
        game.set_difficulty("medium")


def test_check_answer_high_low_correct(capsys):
    assert game.check_answer(50, 10, 5) == 4
    assert "Too high" in capsys.readouterr().out
    assert game.check_answer(5, 10, 4) == 3
    assert "Too low" in capsys.readouterr().out
    assert game.check_answer(10, 10, 3) == 3
    assert "You got it" in capsys.readouterr().out


def _run(monkeypatch, inputs, answer=42):
    monkeypatch.setattr(game.random, "randint", lambda a, b: answer)
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _="": next(it))
    game.play_game()


def test_play_game_win(monkeypatch, capsys):
    _run(monkeypatch, ["easy", "abc", "500", "10", "42"])
    assert "You got it" in capsys.readouterr().out


def test_play_game_lose(monkeypatch, capsys):
    _run(monkeypatch, ["bogus", "hard"] + ["1"] * HARD_ATTEMPTS)
    assert "You lose" in capsys.readouterr().out

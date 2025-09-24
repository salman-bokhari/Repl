from calculator import repl
import pytest

def run_repl_with_inputs(monkeypatch, inputs):
    inputs_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_iter))
    repl.run()

def test_repl_exit(monkeypatch, capsys):
    """Exit immediately with 'exit'."""
    run_repl_with_inputs(monkeypatch, ["exit"])
    captured = capsys.readouterr()
    assert "Welcome to CLI Calculator!" in captured.out
    assert "Goodbye!" in captured.out

def test_repl_keyboard_interrupt(monkeypatch, capsys):
    """KeyboardInterrupt exits gracefully."""
    def fake_input(_):
        raise KeyboardInterrupt
    monkeypatch.setattr("builtins.input", fake_input)
    repl.run()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out

def test_invalid_operation(monkeypatch, capsys):
    """Invalid operation input handled."""
    run_repl_with_inputs(monkeypatch, ["%", "exit"])
    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out

def test_invalid_numbers(monkeypatch, capsys):
    """Non-numeric input handled."""
    run_repl_with_inputs(monkeypatch, ["+", "a", "b", "exit"])
    captured = capsys.readouterr()
    assert "Invalid input" in captured.out

def test_division_by_zero(monkeypatch, capsys):
    """Division by zero handled."""
    run_repl_with_inputs(monkeypatch, ["/", "5", "0", "exit"])
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out

def test_empty_operation(monkeypatch, capsys):
    """Empty string operation handled."""
    run_repl_with_inputs(monkeypatch, ["", "exit"])
    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out

def test_whitespace_input(monkeypatch, capsys):
    """Whitespace operation handled."""
    run_repl_with_inputs(monkeypatch, ["   ", "exit"])
    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out

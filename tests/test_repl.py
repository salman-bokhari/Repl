import pytest
from calculator import repl

def run_repl_with_inputs(monkeypatch, inputs):
    inputs_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_iter))
    repl.run()

def test_repl_exit(monkeypatch, capsys):
    run_repl_with_inputs(monkeypatch, ["exit"])
    captured = capsys.readouterr()
    assert "Welcome to CLI Calculator!" in captured.out
    assert "Goodbye!" in captured.out

def test_repl_keyboard_interrupt(monkeypatch, capsys):
    def fake_input(_):
        raise KeyboardInterrupt
    monkeypatch.setattr("builtins.input", fake_input)
    repl.run()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out

def test_invalid_operation(monkeypatch, capsys):
    run_repl_with_inputs(monkeypatch, ["%", "exit"])
    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out

def test_invalid_numbers(monkeypatch, capsys):
    run_repl_with_inputs(monkeypatch, ["+", "a", "b", "exit"])
    captured = capsys.readouterr()
    assert "Invalid input" in captured.out

def test_division_by_zero(monkeypatch, capsys):
    run_repl_with_inputs(monkeypatch, ["/", "5", "0", "exit"])
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out

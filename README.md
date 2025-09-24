# CLI Calculator

A simple command-line calculator application with REPL interface.

## Features
- Addition, subtraction, multiplication, division
- Input validation and error handling
- REPL interface for continuous use

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python -m calculator.repl
```

## Test
```bash
pytest --cov=calculator --cov-fail-under=100
```

# Python Unit Testing Practice

A small QA-oriented Python project demonstrating automated testing with pytest.

## Project Goal

The purpose of this project is to demonstrate:

* Writing simple Python functions
* Creating automated tests with pytest
* Using parameterized test cases
* Handling valid and invalid inputs
* Applying basic QA testing principles

## Technologies

* Python 3
* Pytest
* Git
* GitHub

## Project Description

This project contains a simple function that classifies a day number as:

* Workday (`Arbeitstag`)
* Weekend (`Wochenende`)
* Invalid weekday (`Ungültiger Wochentag`)

The functionality is covered by automated tests written with pytest.

## Project Structure

```text
src/
    week_schedule.py

tests/
    test_week_schedule.py
```

## Running Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
python -m pytest
```

## Test Coverage

The automated tests verify:

* Valid weekdays (1–5)
* Weekend days (6–7)
* Invalid inputs (0, 8, -1, 100)

A total of 11 test cases are executed automatically.

## Example

```python
get_day_type(1)
# Arbeitstag

get_day_type(6)
# Wochenende

get_day_type(100)
# Ungültiger Wochentag
```

## Author

Albert Lalazaryan

GitHub: https://github.com/lalazaryanqa

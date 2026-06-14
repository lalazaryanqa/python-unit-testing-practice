# Python Unit Testing Practice

A small QA-oriented Python project demonstrating automated testing with pytest.

## Project Goal

The purpose of this project is to demonstrate:

- Python fundamentals
- Test design
- Automated testing with pytest
- Parameterized test cases
- Basic QA engineering practices

## Technologies

- Python
- Pytest
- Git
- GitHub

## Project Structure

```text
src/
    week_schedule.py

tests/
    test_week_schedule.py
```

## Running Tests

```bash
pytest
```

## Test Coverage

The tests verify:

- Valid weekdays (1–5)
- Weekend days (6–7)
- Invalid inputs (0, 8, -1, 100)

## Test Result

All tests passed successfully.

```bash
11 passed in 0.03s
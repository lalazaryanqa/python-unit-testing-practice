import pytest

from src.week_schedule import get_day_type


@pytest.mark.parametrize("day_number", [1, 2, 3, 4, 5])
def test_weekdays_return_workday(day_number):
    assert get_day_type(day_number) == "Arbeitstag"


@pytest.mark.parametrize("day_number", [6, 7])
def test_weekend_days_return_weekend(day_number):
    assert get_day_type(day_number) == "Wochenende"


@pytest.mark.parametrize("day_number", [0, 8, -1, 100])
def test_invalid_days_return_error_message(day_number):
    assert get_day_type(day_number) == "Ungültiger Wochentag"
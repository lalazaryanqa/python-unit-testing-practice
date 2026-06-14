def get_day_type(day_number: int) -> str:
    if 1 <= day_number <= 5:
        return "Arbeitstag"

    if day_number in (6, 7):
        return "Wochenende"

    return "Ungültiger Wochentag"
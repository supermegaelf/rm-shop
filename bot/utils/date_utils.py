from datetime import datetime, timedelta
from typing import Optional


def format_date_localized(dt: Optional[datetime], lang: str = "ru") -> str:
    if not dt:
        return "N/A"
    
    day = dt.day
    month = dt.month
    year = dt.year
    
    if lang == "ru":
        months_ru = {
            1: "янв.", 2: "февр.", 3: "мар.", 4: "апр.",
            5: "мая", 6: "июня", 7: "июля", 8: "авг.",
            9: "сент.", 10: "окт.", 11: "нояб.", 12: "дек."
        }
        month_name = months_ru.get(month, str(month))
        return f"{day} {month_name} {year}"
    else:
        months_en = {
            1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
            5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
            9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
        }
        month_name = months_en.get(month, str(month))
        return f"{month_name} {day}, {year}"


def add_months(base_dt: datetime, months_to_add: int) -> datetime:
    """Add calendar months to a datetime, clamping the day to the month's length.

    Preserves tzinfo from base_dt.
    """
    year = base_dt.year
    month = base_dt.month + months_to_add
    day = base_dt.day

    # Normalize year and month
    year += (month - 1) // 12
    month = ((month - 1) % 12) + 1

    # Determine last day of target month by rolling to next month's first day and subtracting 1 day
    if month == 12:
        next_month_first = datetime(year + 1, 1, 1, tzinfo=base_dt.tzinfo)
    else:
        next_month_first = datetime(year, month + 1, 1, tzinfo=base_dt.tzinfo)
    last_day = (next_month_first - timedelta(days=1)).day

    clamped_day = min(day, last_day)
    return base_dt.replace(year=year, month=month, day=clamped_day)



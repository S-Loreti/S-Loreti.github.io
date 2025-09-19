import re
from datetime import datetime, timedelta

def parse_heil(serial):
    try:
        serial = serial.strip()

        # Style 1: E072514528 → Year: 07, Week: 25
        if re.match(r'^[A-Z]\d{9}$', serial):
            return parse_heil_style1(serial)

        # Future styles can be added here
        return "Unrecognized Heil serial format."
    except:
        return "Invalid Heil serial format."

def parse_heil_style1(serial):
    year = int(serial[1:3])
    week = int(serial[3:5])

    # Determine century: assume 1900s if year > 30, else 2000s
    full_year = 1900 + year if year > 30 else 2000 + year

    if 1 <= week <= 53:
        return format_week_date(full_year, week)
    return "Invalid week in Heil serial."

def format_week_date(year, week):
    # ISO week logic: Jan 4 is always in week 1
    jan4 = datetime(year, 1, 4)
    start_of_week = jan4 + timedelta(weeks=week - 1)
    return start_of_week.strftime("Week %U (%B %Y)")

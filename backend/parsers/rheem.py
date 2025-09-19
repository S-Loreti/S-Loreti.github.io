import re
from datetime import datetime, timedelta

def parse_rheem(serial):
    try:
        serial = serial.strip()

        # Style 1: W291013412 → Year: 10, Week: 29
        if re.match(r'^[A-Z]\d{9}$', serial):
            return parse_rheem_style1(serial)

        # Future styles can be added here
        return "Unrecognized Rheem serial format."
    except:
        return "Invalid Rheem serial format."

def parse_rheem_style1(serial):
    year = int(serial[3:5])
    week = int(serial[1:3])

    # Determine century: assume 1900s if year > 30, else 2000s
    full_year = 1900 + year if year > 30 else 2000 + year

    if 1 <= week <= 53:
        return format_week_date(full_year, week)
    return "Invalid week in Rheem serial."

def format_week_date(year, week):
    # ISO week logic: Jan 4 is always in week 1
    jan4 = datetime(year, 1, 4)
    start_of_week = jan4 + timedelta(weeks=week - 1)
    return start_of_week.strftime("Week %U (%B %Y)")

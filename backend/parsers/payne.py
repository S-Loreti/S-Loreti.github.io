import re
from datetime import datetime, timedelta

def parse_payne(serial):
    try:
        serial = serial.strip()

        # Style 1: 850304091 → Year: 85, Month: 03
        if re.match(r'^\d{9}$', serial):
            return parse_payne_style1(serial)

        # Style 2: 4006A17330 → Year: 06, Week: 40
        if re.match(r'^\d{4}[A-L]\d{5}$', serial):
            return parse_payne_style2(serial)

        return "Unrecognized Payne serial format."
    except:
        return "Invalid Payne serial format."

def parse_payne_style1(serial):
    year = int(serial[0:2])
    month = int(serial[2:4])

    # Determine century: assume 1900s if year > 30, else 2000s
    full_year = 1900 + year if year > 30 else 2000 + year

    if 1 <= month <= 12:
        return format_date(full_year, month)
    return "Invalid month in Payne serial."

def parse_payne_style2(serial):
    year = int(serial[2:4])
    week = int(serial[0:2])

    # Determine century: assume 1900s if year > 30, else 2000s
    full_year = 1900 + year if year > 30 else 2000 + year

    if 1 <= week <= 53:
        return format_week_date(full_year, week)
    return "Invalid week in Payne serial."

def format_week_date(year, week):
    # ISO week logic: Jan 4 is always in week 1
    jan4 = datetime(year, 1, 4)
    start_of_week = jan4 + timedelta(weeks=week - 1)
    return start_of_week.strftime("Week %U (%B %Y)")

def format_date(year, month):
    return datetime(year, month, 1).strftime("%B %Y")
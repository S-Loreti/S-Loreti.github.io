import re
from datetime import datetime, timedelta

def parse_trane(serial):
    try:
        serial = serial.strip()

        # Style 1a: 91531S41F → Year: 9 (2009), Week: 15
        if re.match(r'^\d{5}[A-Z0-9]{4}$', serial):
            return parse_trane_style1a(serial)

        # Style 1b: 10161KEDAA → Year: 10 (2010), Week: 16
        if re.match(r'^\d{5}[A-Z]{5}$', serial):
            return parse_trane_style1b(serial)

        # Style 2: 130313596L → Year: 13 (2013), Week: 03
        if re.match(r'^\d{9}[A-Z]$', serial):
            return parse_trane_style2(serial)

        return "Unrecognized Trane serial format."
    except:
        return "Invalid Trane serial format."

def parse_trane_style1a(serial):
    year_digit = int(serial[0])
    week = int(serial[1:3])
    full_year = 2000 + year_digit

    if 1 <= week <= 53:
        return format_week_date(full_year, week)
    return "Invalid week in Trane serial (Style 1a)."

def parse_trane_style1b(serial):
    year = int(serial[0:2])
    week = int(serial[2:4])
    full_year = 2000 + year

    if 1 <= week <= 53:
        return format_week_date(full_year, week)
    return "Invalid week in Trane serial (Style 1b)."

def parse_trane_style2(serial):
    year = int(serial[0:2])
    week = int(serial[2:4])
    full_year = 2000 + year

    if 1 <= week <= 53:
        return format_week_date(full_year, week)
    return "Invalid week in Trane serial (Style 2)."

def format_week_date(year, week):
    jan4 = datetime(year, 1, 4)
    start_of_week = jan4 + timedelta(weeks=week - 1)
    return start_of_week.strftime("Week %V (%B %Y)")

def format_date(year, month):
    return datetime(year, month, 1).strftime("%B %Y")

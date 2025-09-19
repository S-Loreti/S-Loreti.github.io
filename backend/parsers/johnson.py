import re
from datetime import datetime

def parse_johnson(serial):
    try:
        serial = serial.strip()

        # Style 1: 4140720328 → Year: 03, Week: 28
        if re.match(r'^\d{10}$', serial):
            return parse_johnson_style1(serial)

        # Style 2: 1606B13871 → Year: 06, Month: B
        if re.match(r'^\d{4}[A-L]\d{5}$', serial):
            return parse_johnson_style2(serial)

        return "Unrecognized Johnson serial format."
    except:
        return "Invalid Johnson serial format."

def parse_johnson_style1(serial):
    year = int(serial[6:8])
    week = int(serial[8:10])
    full_year = 1900 + year if year > 30 else 2000 + year

    if 1 <= week <= 53:
        return format_week_date(full_year, week)
    return "Invalid week in Johnson serial."

def parse_johnson_style2(serial):
    year = int(serial[2:4])
    month_code = serial[4].upper()

    full_year = 1900 + year if year > 30 else 2000 + year
    month_map = {
        'A': 'January', 'B': 'February', 'C': 'March', 'D': 'April',
        'E': 'May', 'F': 'June', 'G': 'July', 'H': 'August',
        'J': 'September', 'K': 'October', 'L': 'November', 'M': 'December'
    }

    if month_code in month_map:
        month_name = month_map[month_code]
        return f"{month_name} {full_year}"
    return "Invalid month code in Johnson serial."

def format_week_date(year, week):
    start_of_week = datetime.fromisocalendar(year, week, 1)
    return start_of_week.strftime(f"Week {week} (%B %Y)")

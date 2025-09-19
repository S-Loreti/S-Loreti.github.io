import re
from datetime import datetime

def parse_goodman(serial):
    try:
        serial = serial.strip()

        # Style 1: 9704011000 → YYMMxxxxxx
        if re.match(r'^\d{10}$', serial):
            return parse_goodman_style1(serial)

        # Future styles can be added here with new regex patterns
        return "Unrecognized Goodman serial format."
    except:
        return "Invalid Goodman serial format."

def parse_goodman_style1(serial):
    year = int(serial[0:2])
    month = int(serial[2:4])

    # Determine century: assume 1900s if year > 30, else 2000s
    full_year = 1900 + year if year > 30 else 2000 + year

    if 1 <= month <= 12:
        return format_date(full_year, month)
    return "Invalid month in Goodman serial."

def format_date(year, month):
    return datetime(year, month, 1).strftime("%B %Y")

import re
from datetime import datetime

def parse_lennox(serial):
    try:
        # Style 1: 1606B13871 -or- 5899L17212 → xYMYxxxxxx
        if re.match(r'^\d{4}[A-Z]\d{5}', serial):
            return parse_lennox_style1(serial)

        return "Invalid Lennox serial format."
    except:
        return "Invalid Lennox serial format."

def parse_lennox_style1(serial):
    year_digits = serial[2:4]
    year = int(year_digits)
    full_year = 2000 + year if year <= 49 else 1900 + year

    month_map = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12
    }
    month_letter = serial[4]
    month = month_map.get(month_letter)
    if not month:
        return "Invalid month letter"
    
    return format_date(full_year, month)

def format_date(year, month):
    if 1 <= month <= 12:
        return datetime(year, month, 1).strftime("%B %Y")
    return "Invalid month"
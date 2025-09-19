import re
from datetime import datetime

def parse_champion(serial):
    try:
        # Style 1: E07141664 → MYYxxxxxx
        if re.match(r'^[A-Z]\d{6}', serial):
            return parse_champion_style1(serial)
        
        # Style 2: W1B7400526 → xYMYxxxxxx
        elif re.match(r'^[A-Z]\d[A-Z]\d{6}', serial):
            return parse_champion_style2(serial)

        return "Invalid Champion serial format."
    except:
        return "Invalid Champion serial format."

def parse_champion_style1(serial):
    month_map = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'F': 5, 'H': 6,
        'J': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11, 'P': 12
    }
    year = int(serial[1:3])
    full_year = 2000 + year if year <= 49 else 1900 + year
    month_letter = serial[0].upper()
    month = month_map.get(month_letter)
    if not month:
        return "Invalid month letter"

    return format_date(full_year, month)

def parse_champion_style2(serial):
    year_digits = serial[1] + serial[3]
    year = int(year_digits)
    full_year = 2000 + year if year <= 49 else 1900 + year

    month_map = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'K': 9, 'L': 10, 'M': 11, 'N': 12
    }
    month_letter = serial[2]
    month = month_map.get(month_letter)
    if not month:
        return "Invalid month letter"
    
    return format_date(full_year, month)

def format_date(year, month):
    if 1 <= month <= 12:
        return datetime(year, month, 1).strftime("%B %Y")
    return "Invalid month"
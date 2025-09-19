import re
from datetime import datetime

def parse_armstrong(serial):
    try:
        # Style 1: 4607B20058 → xxYYMxxxx...
        if re.match(r'^\d{4}', serial):
            return parse_armstrong_style1(serial)
        
        # Style 2: A25175KKA → xxxxxMYx...
        elif re.match(r'^[A-Z]', serial):
            return parse_armstrong_style2(serial)

        return "Invalid Armstrong serial format."
    except:
        return "Invalid Armstrong serial format."

def parse_armstrong_style1(serial):
    month_map = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12
    }
    year = int(serial[2:4])
    full_year = 2000 + year if year <= 49 else 1900 + year
    month_letter = serial[4].upper()
    month = month_map.get(month_letter)
    if not month:
        return "Invalid month letter"

    return format_date(full_year, month)


def parse_armstrong_style2(serial):
    month_map = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12
    }

    year_map = {
        '8': 1978, '9': 1979,
        'A': 1980, 'B': 1981, 'C': 1982, 'D': 1983,
        'E': 1984, 'F': 1985, 'G': 1986, 'H': 1987,
        'J': 1988, 'K': 1989, 'L': 1990, 'M': 1991, 'N': 1992
    }

    year_code = serial[7].upper()
    full_year = year_map.get(year_code)
    if not full_year:
        return "Invalid year code"

    month_letter = serial[6].upper()
    month = month_map.get(month_letter)
    if not month:
        return "Invalid month letter"

    return format_date(full_year, month)


def format_date(year, month):
    if 1 <= month <= 12:
        return datetime(year, month, 1).strftime("%B %Y")
    return "Invalid month"
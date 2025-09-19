import re
from datetime import datetime

def parse_aaon(serial):
    try:
        # Style 1: 200108AKG26241 → YYYYMMxxxx...
        if re.match(r'^\d{6}', serial):
            return parse_aaon_style1(serial)
        
        # Style 2: 97JKGK153 → yyLxxxx...
        elif re.match(r'^\d{2}[A-Z]', serial):
            return parse_aaon_style2(serial)

        # Style 3: AKEC08701 → AAAAyyMMx...
        elif re.match(r'^[A-Z]{4}\d{5}', serial):
            return parse_aaon_style3(serial)

        return "Invalid AAON serial format."
    except:
        return "Invalid AAON serial format."

def parse_aaon_style1(serial):
    year = int(serial[0:4])
    month = int(serial[4:6])
    return format_date(year, month)

def parse_aaon_style2(serial):
    month_map = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12
    }
    year = int(serial[0:2])
    full_year = 2000 + year if year <= 49 else 1900 + year
    month_letter = serial[2].upper()
    month = month_map.get(month_letter)
    if not month:
        return "Invalid month letter"
    return format_date(full_year, month)

def parse_aaon_style3(serial):
    year = int(serial[5:7])
    full_year = 2000 + year if year <= 49 else 1900 + year
    month = int(serial[7:9])
    return format_date(full_year, month)

def format_date(year, month):
    if 1 <= month <= 12:
        return datetime(year, month, 1).strftime("%B %Y")
    return "Invalid month"

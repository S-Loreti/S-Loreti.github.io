import re
from datetime import datetime

def parse_bryant(serial):
    if len(serial) < 5:
        return "Serial number too short."

    try:
        # Style 1: 0709G10932 → WWYYAxxxxx
        if re.match(r'^\d{4}[A-Z]', serial):
            return parse_bryant_style1(serial)

        # Style 2: 850304091 → YYMMxxxx
        elif re.match(r'^\d{4}', serial):
            return parse_bryant_style2(serial)
        
        # Style 3: W4D14008 → MYxxxxxx
        elif re.match(r'^[A-Z]\d[A-Z]\d{5}', serial):
            return parse_bryant_style3(serial)
        
        # Style 4: A167890 → MYxxxxxx
        elif re.match(r'^[A-Z]\d{6}', serial):
            return parse_bryant_style4(serial)
        
        # Style 5: 46U152456 or 2W13270 (1–2 digits + letter)
        elif re.match(r'^\d{1,2}[A-Z]\w{4,7}$', serial):
            return parse_bryant_style5(serial)

        return "Unrecognized Bryant format."
    except:
        return "Invalid Bryant serial format."

def parse_bryant_style1(serial):
    week = int(serial[0:2])
    year_prefix = "19" if int(serial[2:4]) > 30 else "20"
    year = int(year_prefix + serial[2:4])

    # Get the first day of the given ISO week
    first_day_of_week = datetime.strptime(f'{year}-W{week:02}-1', "%Y-W%W-%w")
    month_name = first_day_of_week.strftime("%B")
    return f"{month_name} {year}"

def parse_bryant_style2(serial):
    year_prefix = "19" if int(serial[0:2]) > 30 else "20"
    year = int(year_prefix + serial[0:2])
    month = int(serial[2:4])
    if 1 <= month <= 12:
        return datetime(year, month, 1).strftime("%B %Y")
    return "Invalid month"

def parse_bryant_style3(serial):
    month_map = {
        'M': 1, 'N': 2, 'P': 3, 'Q': 4, 'R': 5, 'S': 6,
        'T': 7, 'V': 8, 'W': 9, 'X': 10, 'Y': 11, 'Z': 12
    }

    year_map = {
        '0': 1980, '1': 1981,
        '2': 1982, '3': 1983, '4': 1984, 
    }

    year_code = serial[1]
    full_year = year_map.get(year_code)
    if not full_year:
        return "Invalid year code"

    month_letter = serial[0].upper()
    month = month_map.get(month_letter)
    if not month:
        return "Invalid month letter"

    return format_date(full_year, month)

def parse_bryant_style4(serial):
    month_map = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12
    }
    year_map = {
        '0': 1970, '1': 1971, '2': 1972, '3': 1973, '4': 1974, 
        '5': 1975, '6': 1976, '7': 1977, '8': 1978, '9': 1979, 
    }
    year_code = serial[1]
    full_year = year_map.get(year_code)
    if not full_year:
        return "Invalid year code"

    month_letter = serial[0].upper()
    month = month_map.get(month_letter)
    if not month:
        return "Invalid month letter"

    return format_date(full_year, month)

def parse_bryant_style5(serial):
    match = re.match(r'^(\d{1,2})([A-Z])\w{4,7}$', serial)
    if not match:
        return "Invalid Style 5 format."

    week_str, letter = match.groups()
    week = int(week_str)
    if not (1 <= week <= 52):
        return "Invalid week number."

    year_map = {
        'L': 1960, 'M': 1961, 'N': 1962, 'P': 1963, 'R': 1964,
        'S': 1965, 'T': 1966, 'U': 1967, 'V': 1968, 'W': 1969,
        'X': 1970, 'Y': 1971, 'A': 1972, 'B': 1973, 'C': 1974,
        'D': 1975, 'E': 1976, 'F': 1977, 'G': 1978, 'H': 1979
    }
    if letter not in year_map:
        return "Invalid year letter."

    year = year_map[letter]
    first_day_of_week = datetime.strptime(f'{year}-W{week:02}-1', "%Y-W%W-%w")
    return f"{first_day_of_week.strftime('%B')} {year}"


def format_date(year, month):
    if 1 <= month <= 12:
        return datetime(year, month, 1).strftime("%B %Y")
    return "Invalid month"

import re
from datetime import datetime

def parse_york(serial):
    try:
        serial = serial.strip()

        # Style 1: W0K5896070 → Year from 2nd & 4th digits, Month from 3rd letter
        if re.match(r'^[A-Z]\d[A-Z]\d{7}$', serial):
            return parse_york_style1(serial)

        # Style 2: WAKM011379 → Year from 3rd letter, Month from 2nd letter
        if re.match(r'^[A-Z]{4}\d{6}$', serial):
            return parse_york_style2(serial)

        return "Unrecognized York serial format."
    except:
        return "Invalid York serial format."

def parse_york_style1(serial):
    year_digit_1 = serial[1]
    year_digit_2 = serial[3]
    month_letter = serial[2]

    try:
        year = int(year_digit_1 + year_digit_2)
        full_year = 2000 + year
        month = month_letter_to_number(month_letter)

        if month:
            return format_date(full_year, month)
        return "Invalid month letter in York serial (Style 1)."
    except:
        return "Invalid year digits in York serial (Style 1)."

def parse_york_style2(serial):
    month_letter = serial[1]
    year_letter = serial[2]

    month = month_letter_to_number(month_letter)
    years = year_letter_to_year_options(year_letter)

    if not month:
        return "Invalid month letter in York serial (Style 2)."
    if not years:
        return "Invalid year letter in York serial (Style 2)."

    month_name = datetime(2000, month, 1).strftime("%B")
    return f"{month_name}, possibly in {years[0]} or {years[1]}"


def month_letter_to_number(letter):
    month_map = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'K': 9, 'L': 10, 'M': 11, 'N': 12
    }
    return month_map.get(letter.upper())

def year_letter_to_year_options(letter):
    year_map = {
        'A': [1971, 1992], 'B': [1972, 1993], 'C': [1973, 1994], 'D': [1974, 1995],
        'E': [1975, 1996], 'F': [1976, 1997], 'G': [1977, 1998], 'H': [1978, 1999],
        'J': [1979, 2000], 'K': [1980, 2001], 'L': [1981, 2002], 'M': [1982, 2003],
        'N': [1983, 2004], 'P': [1984], 'R': [1985], 'S': [1986], 'T': [1987],
        'V': [1988], 'W': [1989], 'X': [1990], 'Y': [1991]
    }
    return year_map.get(letter.upper())

def format_date(year, month):
    return datetime(year, month, 1).strftime("%B %Y")

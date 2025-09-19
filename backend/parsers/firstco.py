import re
from datetime import datetime

def parse_firstco(serial):
    try:
        # Normalize input: remove spaces and uppercase
        serial = serial.replace(" ", "").upper()

        # Match both styles: S05A881350 or F05FC032358927092
        if re.match(r'^[A-Z]\d{2}[A-Z0-9]+$', serial):
            return parse_firstco_style(serial)

        return "Invalid First Co serial format."
    except:
        return "Invalid First Co serial format."

def parse_firstco_style(serial):
    year_letter = serial[0]
    month_digits = serial[1:3]

    year_map = {
        'A': [1994, 2017], 'B': [1995, 2018], 'C': [1996, 2019], 'D': [1997, 2020],
        'E': [1998, 2021], 'F': [1999, 2022], 'G': [2000, 2023], 'H': [2001, 2024],
        'J': [2002, 2025], 'K': [2003, 2026], 'L': [2004, 2027], 'M': [2005, 2028],
        'N': [2006, 2029], 'P': [2007, 2030], 'R': [2008], 'S': [2009], 'T': [2010],
        'U': [2011], 'V': [2012], 'W': [2013], 'X': [2014], 'Y': [2015], 'Z': [2016]
    }

    possible_years = year_map.get(year_letter)
    if not possible_years:
        return "Invalid year letter"

    try:
        month = int(month_digits)
        if not (1 <= month <= 12):
            return "Invalid month digits"
    except ValueError:
        return "Invalid month digits"

    # Format both possible dates
    formatted_dates = [
        datetime(year, month, 1).strftime("Manufactured: %B %Y")
        for year in possible_years
    ]

    return f"Due to First Co's serial number system the following are possible manufacture dates:\n- " + "\n- ".join(formatted_dates)

import re
from datetime import datetime

def parse_evapco(serial):
    try:
        # Evapco format: 10-399266 → YY-xxxxxx
        if re.match(r'^\d{2}-\d{6}', serial):
            return parse_evapco_style(serial)
        return "Invalid Evapco serial format."
    except:
        return "Invalid Evapco serial format."

def parse_evapco_style(serial):
    year_prefix = int(serial[0:2])
    full_year = 2000 + year_prefix  # Evapco format starts at 2000

    return format_date(full_year)

def format_date(year):
    return datetime(year, 1, 1).strftime("%Y")

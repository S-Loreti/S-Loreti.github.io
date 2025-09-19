import re
from datetime import datetime

def parse_amana(serial):
    """
    Supports three known formats:
    - Style 1: 0109145052 → YYMMxxxxxx
    - Style 2: 96-90391   → YY-xxxxx
    - Style 3: 040590391  → YYMMxxxxx
    """
    if len(serial) < 6:
        return "Serial number too short."

    try:
        # Style 1: YYMMxxxxxx or YYMMxxxxx
        if re.match(r'^\d{4}', serial):
            return parse_amana_style1(serial)

        # Style 2: YY-xxxxx
        elif re.match(r'^\d{2}-\d{5}$', serial):
            return parse_amana_style2(serial)

        return "Unrecognized Amana serial format."
    except:
        return "Invalid Amana serial format."


# 🔧 Format Parsers

def parse_amana_style1(serial):
    """
    Style 1: 0109145052 → YYMMxxxxxx → September 2011
    """
    year = int(serial[0:2])
    month = int(serial[2:4])
    full_year = 2000 + year if year <= 49 else 1900 + year
    return datetime(full_year, month, 1).strftime("%B %Y")


def parse_amana_style2(serial):
    """
    Style 2: 96-90391 → YY-xxxxx → January 1996
    """
    year = int(serial[0:2])
    full_year = 2000 + year if year <= 49 else 1900 + year
    return datetime(full_year, 1, 1).strftime("%Y")

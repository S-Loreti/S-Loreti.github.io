import re
from datetime import datetime, timedelta

def parse_daikin(serial):
    try:
        # Style 1: FBOU0905048200 → XXXXYYMMxxxxxx
        if re.match(r'^[A-Z]{4}\d{10}', serial):
            return parse_daikin_style1(serial)
        
        # Style 2: 20444501000138 → YYYYWWxxxxxxx
        elif re.match(r'^\d{14}', serial):
            return parse_daikin_style2(serial)

        return "Invalid Daikin serial format."
    except:
        return "Invalid Daikin serial format."

def parse_daikin_style1(serial):
    year = int(serial[4:6])
    month = int(serial[6:8])
    full_year = 2000 + year if year <= 49 else 1900 + year
    return format_date(full_year, month)

def parse_daikin_style2(serial):
    raw_year = int(serial[0:4])
    week = int(serial[4:6])

    # Daikin offset: 2043 = year 2000
    full_year = raw_year - 43
    return format_week_date(full_year, week)

def format_date(year, month):
    if 1 <= month <= 12:
        return datetime(year, month, 1).strftime("%B %Y")
    return "Invalid month"

def format_week_date(year, week):
    if 1 <= week <= 53:
        # ISO week starts on Monday
        first_day = datetime(year, 1, 1)
        # Adjust to the first Monday of the year
        days_to_monday = (7 - first_day.weekday()) % 7
        first_monday = first_day + timedelta(days=days_to_monday)
        manufacture_date = first_monday + timedelta(weeks=week - 1)
        return manufacture_date.strftime("Week %U (%B %Y)")
    return "Invalid week"

import re
from datetime import datetime, timedelta

def parse_icp(serial):
    try:
        serial = serial.strip()

        # Style 1: G051650885 → Year: 05, Week: 16
        if re.match(r'^[A-Z]\d{9}$', serial):
            return parse_icp_style1(serial)

        # Future styles can be added here
        return "Unrecognized ICP serial format."
    except:
        return "Invalid ICP serial format."

def parse_icp_style1(serial):
    year = int(serial[1:3])
    week = int(serial[3:5])

    # Determine century: assume 1900s if year > 30, else 2000s
    full_year = 1900 + year if year > 30 else 2000 + year

    if 1 <= week <= 53:
        return format_week_date(full_year, week)
    return "Invalid week in ICP serial."

def format_week_date(year, week):
    # ISO weeks start on Monday, week 1 is the first week with a Thursday
    first_day = datetime(year, 1, 4)  # Jan 4 is always in week 1
    start_of_week = first_day + timedelta(weeks=week - 1)
    return start_of_week.strftime("Week %U (%B %Y)")

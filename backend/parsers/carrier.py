import re
from datetime import datetime

def parse_carrier(serial):
    if len(serial) < 5:
        return "Serial number too short."

    try:
        # Style 1: 4006A17330 → WWYYAxxxxx
        if re.match(r'^\d{4}[A-Z]', serial):
            return parse_carrier_style1(serial)

        # Style 2: 850304091 → YYMMxxxx
        elif re.match(r'^\d{4}', serial):
            return parse_carrier_style2(serial)

        return "Unrecognized Carrier format."
    except:
        return "Invalid Carrier serial format."

def parse_carrier_style1(serial):
    week = int(serial[0:2])
    year_prefix = "19" if int(serial[2:4]) > 30 else "20"
    year = int(year_prefix + serial[2:4])

    # Get the first day of the given ISO week
    first_day_of_week = datetime.strptime(f'{year}-W{week:02}-1', "%Y-W%W-%w")
    month_name = first_day_of_week.strftime("%B")
    return f"{month_name} {year}"

def parse_carrier_style2(serial):
    year_prefix = "19" if int(serial[0:2]) > 30 else "20"
    year = int(year_prefix + serial[0:2])
    month = int(serial[2:4])
    if 1 <= month <= 12:
        return datetime(year, month, 1).strftime("%B %Y")
    return "Invalid month"


import re
from typing import Tuple

## -- Task 3 (IN3110 optional, IN4110 required) -- ##

# create array with all names of months
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

...


def get_date_patterns() -> Tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """

    jan = r"\b[jJ]an(?:uary)?\b"
    feb = r"\b[fF]eb(?:ruary)?\b"
    mar = r"\b[mM]ar(?:ch)?\b"
    apr = r"\b[aA]pr(?:il)?\b"
    may = r"\b[mM]ay\b"
    jun = r"\b[jJ]un(?:e)?\b"
    jul = r"\b[jJ]ul(?:y)?\b"
    aug = r"\b[aA]ug(?:ust)?\b"
    sep = r"\b[sS]ep(?:ptember)?\b"
    octo = r"\b[oO]ct(?:ober)?\b"
    nov = r"\b[nN]ov(?:ember)?\b"
    dec = r"\b[dD]ec(?:ember)?\b"

    # Regex to capture days, months and years with numbers
    # year should accept a 4-digit number between at least 1000-2029
    year = r"?P<year>\b(1\d\d\d|20[0-2]\d)\b"
    # month should accept month names or month numbers
    month = rf"(?P<month>({jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|{octo}|{nov}|{dec}))"
    # day should be a number, which may or may not be zero-padded
    day = r"?P<day>\b([0-2]?\d|3[01])\,?\b"
    
    iso_month = r"?P<iso_month>\b(0\d|1[0-2])"

    return year, month, day, iso_month


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    You don't need to use this function,
    but you may find it useful.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """
    # If already digit do nothing
    if s.isdigit():
        return

    # Convert to number as string
    for i in range(len(month_names)):
        if s == month_names[i]:
            return f"{i+1}"


def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    You don't need to use this function,
    but you may find it useful.
    """
    
    return f"0{n}"


def find_dates(text: str, output: str = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
    return:
        results (list): A list with all the dates found
    """
    
    # Fetches patterns to use in date formats.
    year, month, day, iso_month = get_date_patterns()

    # Date on format YYYY/MM/DD - ISO
    ISO = rf"\b({year})-({iso_month})-({day})\b"

    # Date on format DD/MM/YYYY
    DMY = rf"({day})\s({month})\s({year})"

    # Date on format MM/DD/YYYY
    MDY = rf"({month})\s({day})\s({year})"

    # Date on format YYYY/MM/DD
    YMD = rf"({year})\s({month})\s({day})"

    # list with all supported formats
    formats = [ISO, DMY, MDY, YMD]
    dates = []

    # find all dates in any format in text
    dates_ISO = re.findall(ISO, text)
    dates_DMY = re.findall(DMY, text)
    dates_MDY = re.findall(MDY, text)
    dates_YMD = re.findall(YMD, text)
    
    # These 4 for-loops will convert all dates to valid dates, and 
    # append the dates to the list 'dates'.
    # Bruker re.sub for enten reorder eller erstatting.
    for date_element in dates_ISO:
        date_element = re.sub(r"-", r"/", date_element)
        dates.append(date_element)
        
    # Reorder required.
    for date_element in dates_DMY:
        date_element = re.sub(DMY, r"\3/\2/\1", date_element)
        date_element = re.sub(r"\s", r"/", date_element)
    
    # Reorder required
    for date_element in dates_MDY:
        date_element = re.sub(MDY, r"\3/\1/\2", date_element)
        date_element = re.sub(r",\s", r"", date_element)
        date_element = re.sub(r"/", r"\s", date_element)
    
    for date_element in dates_YMD:
        date_element = re.sub(r"\s", r"/", date_element)
        
    
    
    # Write to file if wanted
    if output:
        ...

    return dates

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

    jan = r"[jJ]an(?:uary)?"
    feb = r"[fF]eb(?:ruary)?"
    mar = r"[mM]ar(?:ch)?"
    apr = r"[aA]pr(?:il)?"
    may = r"[mM]ay"
    jun = r"[jJ]un(?:e)?"
    jul = r"[jJ]ul(?:y)?"
    aug = r"[aA]ug(?:ust)?"
    sep = r"[sS]ep(?:ptember)?"
    octo = r"[oO]ct(?:ober)?"
    nov = r"[nN]ov(?:ember)?"
    dec = r"[dD]ec(?:ember)?"

    # Regex to capture days, months and years with numbers
    # year should accept a 4-digit number between at least 1000-2029
    year = r"(?P<year>(?:1\d\d\d|20[0-2]\d))"
    # month should accept month names or month numbers
    month = rf"(?P<month>(?:{jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|{octo}|{nov}|{dec}))"
    # day should be a number, which may or may not be zero-padded
    day = r"(?P<day>(?:[0-2]?\d|3[01])\,?)"
    
    iso_month = r"(?P<iso_month>0\d|1[0-2])"

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
    
    # Fetches grouped patterns to use in date formats.
    # No need to specify the groups in the formats.
    year, month, day, iso_month = get_date_patterns()

    # Date on format YYYY/MM/DD - ISO
    ISO = rf"\b{year}-{iso_month}-{day}\b"

    # Date on format DD/MM/YYYY
    DMY = rf"\b{day}\s{month}\s{year}\b"

    # Date on format MM/DD/YYYY
    MDY = rf"\b{month}\s{day}\s{year}\b"

    # Date on format YYYY/MM/DD
    YMD = rf"\b{year}\s{month}\s{day}\b"

    # list with all supported formats
    formats = [ISO, DMY, MDY, YMD]
    dates = []

    # find all dates in any format in text
    dates_ISO = re.findall(ISO, text)
    dates_DMY = re.findall(DMY, text)
    dates_MDY = re.findall(MDY, text)
    dates_YMD = re.findall(YMD, text)
    
    
    # Fant ut med denne kodebiten at findall finner alle grupper, men ikke gruppe 0.
    print("ISO dates:\n")
    for i in dates_ISO:
        print(i)
    
    print("\nDMY dates:\n")
    for i in dates_DMY:
        print(i)
        
    print("\nMDY dates:\n")
    for i in dates_MDY:
        print(i)
        
    print("\nYMD dates:\n")
    for i in dates_YMD:
        print(i)
    
    """
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
    """
    
if __name__ == "__main__":
    
    date_text = """
    DMY: 2 January 2020
    MDY: February 12, 1954
    YMD: 2015 March 31
    ISO: 2022-04-15
    """
    
    find_dates(date_text)
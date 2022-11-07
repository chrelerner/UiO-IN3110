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
    day = r"(?P<day>(?:[0-2]?\d|3[01])),?"
    
    iso_month = r"(?P<iso_month>0\d|1[0-2])"

    return year, month, day, iso_month


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

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
        if s[:3] == month_names[i][:3]:
            month_number = f"{i+1}"
            return zero_pad(month_number)


def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'
    """

    if len(n) == 1:
        return f"0{n}"
    return n


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
    ISO = rf"(\b{year}-{iso_month}-{day}\b)"

    # Date on format DD/MM/YYYY
    DMY = rf"(\b{day}\s{month}\s{year}\b)"

    # Date on format MM/DD/YYYY
    MDY = rf"(\b{month}\s{day}\s{year}\b)"

    # Date on format YYYY/MM/DD
    YMD = rf"(\b{year}\s{month}\s{day}\b)"

    dates = []

    # Finds all dates in any format in text
    dates_ISO = re.finditer(ISO, text)
    dates_DMY = re.finditer(DMY, text)
    dates_MDY = re.finditer(MDY, text)
    dates_YMD = re.finditer(YMD, text)
    
    # These 4 for-loops will convert all dates to valid dates, and 
    # append the dates to the list 'dates'.
    for element in dates_ISO:
        element_year = element.group("year")
        element_month = element.group("iso_month")
        element_day = element.group("day")
        
        element_month = zero_pad(element_month)
        element_day = zero_pad(element_day)
        
        correct_date = f"{element_year}/{element_month}/{element_day}"
        dates.append(correct_date)
    
    for element in dates_DMY:
        element_year = element.group("year")
        element_month = element.group("month")
        element_day = element.group("day")
        
        element_month = convert_month(element_month)        
        element_day = zero_pad(element_day)
        
        correct_date = f"{element_year}/{element_month}/{element_day}"
        dates.append(correct_date)
    
    
    for element in dates_MDY:
        element_year = element.group("year")
        element_month = element.group("month")
        element_day = element.group("day")
        
        element_month = convert_month(element_month)        
        element_day = zero_pad(element_day)
        
        correct_date = f"{element_year}/{element_month}/{element_day}"
        dates.append(correct_date)
    
    for element in dates_YMD:
        element_year = element.group("year")
        element_month = element.group("month")
        element_day = element.group("day")
        
        element_month = convert_month(element_month)        
        element_day = zero_pad(element_day)
        
        correct_date = f"{element_year}/{element_month}/{element_day}"
        dates.append(correct_date)
        
    # Write to file if wanted
    if output:
        print(f"Writing to: {output}")
        output_file = open(output, "w", encoding="utf-8")
        output_file.write("Found dates:\n")
        for date in dates:
            output_file.write(f"\n--- {date}\n")
        
    return dates
    
if __name__ == "__main__":
    
    date_text = """
    DMY: 2 January 2020
    MDY: February 12, 1954
    YMD: 2015 March 31
    ISO: 2022-04-15
    """
    
    find_dates(date_text)
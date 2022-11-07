from typing import Dict, Optional

import requests

## -- Task 1 -- ##


def get_html(url: str, params: Optional[Dict] = None, output: Optional[str] = None):
    """Get an HTML page and return its contents.

    Args:
        url (str):
            The URL to retrieve.
        params (dict, optional):
            URL parameters to add.
        output (str, optional):
            (optional) path where output should be saved.
    Returns:
        html (str):
            The HTML of the page, as text.
    """
    
    # Gets the HTML page, and its text string.
    response = requests.get(url, params = params)
    html_str = response.text

    if output:
        # If output is specified, the response txt and url get printed to a
        # txt file with the name in `output`
        print("Writing to file")
        output_file = open(output, "w", encoding="utf-8")
        output_file.write(f"URL: {url}\n\n")
        output_file.write(f"HTML text:\n\n {html_str}")
        
    return html_str

if __name__ == "__main__":
    
    get_html(url="https://en.wikipedia.org/wiki/Studio_Ghibli", output="out_requesting_urls.txt")

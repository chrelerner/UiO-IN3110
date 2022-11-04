import re
from urllib.parse import urljoin

## -- Task 2 -- ##


def find_urls(
    html: str,
    base_url: str = "https://en.wikipedia.org",
    output: str = None,
) -> set:
    """Find all the url links in a html text using regex
    Arguments:
        html (str): html string to parse
    Returns:
        urls (set) : set with all the urls found in html text
    """
    # create and compile regular expression(s)

    # 1. find all the anchor tags, then
    # 2. find the urls href attributes

    # Finds all hrefs in the html text.
    hrefs = find_a_href(html)
    
    # Filters out fragments, and adds base URL to beginning of 
    # uncomplete URLS that start with /.
    for href in hrefs:
        #Filtrer foerst ut hash. Saa fiks /.
        ...
    
    urls = hrefs

    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        output_file = open(output, "w")
        for url in urls:
            output_file.write(f"\n{url}")
        
    return urls


def find_articles(html: str, output=None) -> set:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
    returns:
        - (set) : a set with urls to all the articles found
    """
    urls = find_urls(html)
    
    pattern = ... # Regex pattern to detect wikipedia URLS without ;
    articles = ...

    # Write to file if wanted
    if output:
        ...
    ...
    
# Function derived from find_img_src
def find_a_href (html: str):
    """Find all href attributes of a tags in an HTML string

    Args:
        html (str): A string containing some HTML.

    Returns:
        href_set (set): A set of strings containing 'a' URLs

    The set contains every found href attibute of an 'a' tag in the given HTML.
    """
    
    # a_pat finds all the <a alt="..." src="..."> snippets
    # this finds <a and collects everything up to the closing '>'
    a_pat = re.compile(r"<a[^>]+>", flags=re.IGNORECASE)
    
    # href finds the text between quotes of the `href` attribute
    href_pat = re.compile(r'href="([^"]+)"', flags=re.IGNORECASE)
    href_set = set()
    # first, find all the 'a' tags
    for a_tag in a_pat.findall(html):
        # then, find the href attribute of the 'a', if any
        match = href_pat.search(a_tag)
        if match:
            href_set.add(match.group(1))
            
    return href_set
    


## Regex example
def find_img_src(html: str):
    """Find all src attributes of img tags in an HTML string

    Args:
        html (str): A string containing some HTML.

    Returns:
        src_set (set): A set of strings containing image URLs

    The set contains every found src attibute of an img tag in the given HTML.
    """
    # img_pat finds all the <img alt="..." src="..."> snippets
    # this finds <img and collects everything up to the closing '>'
    img_pat = re.compile(r"<img[^>]+>", flags=re.IGNORECASE)
    # src finds the text between quotes of the `src` attribute
    src_pat = re.compile(r'src="([^"]+)"', flags=re.IGNORECASE)
    src_set = set()
    # first, find all the img tags
    for img_tag in img_pat.findall(html):
        # then, find the src attribute of the img, if any
        match = src_pat.search(img_tag)
        if match:
            src_set.add(match.group(1))
    return src_set

if __name__ == "__main__":
    
    html = """
    <a href="#fragment-only">anchor link</a>
    <a id="some-id" href="/relative/path#fragment">relative link</a>
    <a href="//other.host/same-protocol">same-protocol link</a>
    <a href="https://example.com">absolute URL</a>
    """
    
    hrefs = find_a_href(html)
    
    for i in hrefs:
        print(i + "\n")
    

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

    # Finds all the URLs or URL paths without #-fragments.
    hrefs = find_a_href(html)
    urls = set()
    
    for href in hrefs:
        # Combines base URL with URL path.
        if re.search(r'^/[^/]', href): # If href begins with one /
            full_url = f"{base_url}{href}"
            urls.add(full_url)
            
        # Adds https protocol to the URL.
        elif re.search(r'^//', href): # If href begins with //
            full_url = f"https:{href}"
            urls.add(full_url)
            
        else:
            urls.add(href)
        
    # Writes to file if requested
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
    pattern = r'https://[a-z.]*wikipedia.org/wiki/[^:]+\b' # Regex pattern to detect wikipedia URLs without :
    articles = set()
    
    for url in urls:
        if re.search(pattern, url):
            articles.add(url)

    # Writes to file if wanted
    if output:
        print(f"Writing to: {output}")
        output_file = open(output, "w")
        for article in articles:
            output_file.write(f"\n{article}")
            
    return articles
    

# Function derived from find_img_src
def find_a_href (html: str):
    """Find all href attributes of a tags in an HTML string
    
    Filters out fragments of the URLs. If the href attribute
    only contains a URL fragment, it will be ignored.

    Args:
        html (str): A string containing some HTML.

    Returns:
        href_set (set): A set of strings containing 'a' URLs

    The set contains every found href attibute of an 'a' tag in the given HTML.
    """
    
    #This pattern finds <a and collects everything up to the closing '>'
    a_pat = re.compile(r"<a[^>]+>", flags=re.IGNORECASE)
    
    # This pattern finds the text between quotes of the `href` attribute
    href_pat = re.compile(r'href="([^"#]+)("|#)', flags=re.IGNORECASE)
    href_set = set()
    
    # Checks all the 'a' tags for valid href sections.
    for a_tag in a_pat.findall(html):
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
        print(i)
    
    print("\n")
    urls = find_urls(html)
    
    for i in urls:
        print(i)
        
        
    

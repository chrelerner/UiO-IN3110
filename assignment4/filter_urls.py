import re
from urllib.parse import urljoin
from requesting_urls import get_html

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
    raw_urls = find_urls_inner(html)
    urls = set()
    
    for url in raw_urls:
        # Combines base URL with URL path.
        if re.search(r'^/[^/]', url): # If href begins with one /
            full_url = f"{base_url}{url}"
            urls.add(full_url)
            
        # Adds https protocol to the URL.
        elif re.search(r'^//', url): # If href begins with //
            full_url = f"https:{url}"
            urls.add(full_url)
            
        # Already complete url.
        else:
            urls.add(url)
        
    # Writes to file if requested
    if output:
        print(f"Writing to: {output}")
        output_file = open(output, "w", encoding="utf-8")
        output_file.write("Found URLs:\n")
        for url in urls:
            output_file.write(f"\n- {url}\n")
        
    return urls


def find_articles(html: str, output=None) -> set:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
    returns:
        - (set) : a set with urls to all the articles found
    """
    
    # Finds the URLs and defines patterns to search with.
    urls = find_urls(html)
    pattern_1 = r'https://[a-z.]*wikipedia.org/wiki/(.+)' # Regex pattern to detect wikipedia URLs
    pattern_2 = r':' # Regex pattern to filer out URLs with ':' at the end.
    articles = set()
    
    for url in urls:
        match_1 = re.search(pattern_1, url)
        if match_1:
            match_2 = re.search(pattern_2, match_1.group(1))
            if not match_2:
                articles.add(url)

    # Writes to file if wanted
    if output:
        print(f"Writing to: {output}")
        output_file = open(output, "w", encoding="utf-8")
        output_file.write("Found articles:\n")
        for article in articles:
            output_file.write(f"\n- {article}\n")
            
    return articles
    

# Function derived from find_img_src
def find_urls_inner (html: str):
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
    href_pat = re.compile(r'href="([^"#]+)(?:"|#)', flags=re.IGNORECASE)
    raw_urls = set()
    
    # Checks all the 'a' tags for valid href sections.
    for a_tag in a_pat.findall(html):
        match = href_pat.search(a_tag)
        if match:
            raw_urls.add(match.group(1))
            
    return raw_urls
    


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
    
    #html = """
    #<a href="#fragment-only">anchor link</a>
    #<a id="some-id" href="/relative/path#fragment">relative link</a>
    #<a href="//other.host/same-protocol">same-protocol link</a>
    #<a href="https://example.com">absolute URL</a>
    #"""
    
    html = get_html(url="https://en.wikipedia.org/wiki/Nobel_Prize")
    
    find_urls(html=html, output="out_filter_urls_find_urls.txt")
    
    find_articles(html=html, output="out_filter_urls_find_articles.txt")
    
    
        
        
    

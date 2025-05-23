import requests , urllib, re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def fetch_title_and_favicon(url):
    try:
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.text, "html.parser")
        # Get title
        title = soup.title.string.strip() if soup.title else url
        # Get favicon
        icon_link = soup.find("link", rel=lambda x: x and "icon" in x.lower())
        if icon_link and icon_link.get("href"):
            favicon_url = urljoin(url, icon_link["href"])
        else:
            favicon_url = urljoin(url, "/favicon.ico")
        return title, favicon_url
    except Exception:
        return url, ""  
def clean_and_shorten_summary(text, max_sentences=6):
    # Clean as before
    text = re.sub(r'\|.*\|', '', text)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\*\*.*?\*\*', '', text)
    text = re.sub(r'#+ ', '', text)
    text = re.sub(r'_{2,}', '', text)
    text = re.sub(r'[\(\)\[\]\{\}]', '', text)
    text = re.sub(r'[\|]', '', text)
    text = re.sub(r'(?m)^\s*\*.*$', '', text)
    text = re.sub(r'(?m)^\s*File name:.*$', '', text)
    text = re.sub(r'(?m)^\s*URL Source:.*$', '', text)
    text = re.sub(r'(?m)^\s*Published Time:.*$', '', text)
    text = re.sub(r'(?m)^\s*Search results:.*$', '', text)
    text = re.sub(r'(?m)^\s*Attached URL:.*$', '', text)
    text = re.sub(r'(?m)^\s*\d+\.\s*', '', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    # Split into sentences using punctuation
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Filter: at least 7 words, ends with ., !, or ?, and at least 4 chars before punctuation
    clean_sentences = []
    for s in sentences:
        s = s.strip()
        if (
            len(s.split()) > 6 and
            re.match(r'.{4,}[.!?]$', s)
        ):
            # Exclude sentences that end with 'the .', 'of .', etc.
            if not re.search(r'\b(the|of|in|on|at|for|to|by|with) \.$', s):
                clean_sentences.append(s)
        if len(clean_sentences) == max_sentences:
            break

    summary = ' '.join(clean_sentences)
    return summary if summary else "Summary not available."

def fetch_summary(url, max_sentences=6):
    try:
        api_url = "https://r.jina.ai/" + urllib.parse.quote(url, safe='')
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            raw_summary = response.text.strip()
            return clean_and_shorten_summary(raw_summary, max_sentences)
        else:
            return "Summary not available."
    except Exception as e:
        return f"Error fetching summary: {e}"


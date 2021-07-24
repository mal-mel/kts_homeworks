from bs4 import BeautifulSoup


_black_list = ["script", "style"]


def is_html_contains_tags(html: str, tags: list) -> bool:
    soup = BeautifulSoup(html, "lxml")
    content = "".join(t.strip() for t in soup.find_all(text=True) if t.parent.name not in _black_list)
    for tag in tags:
        if tag in content:
            return True
    return False

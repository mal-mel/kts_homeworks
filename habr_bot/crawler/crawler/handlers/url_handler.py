from urllib.parse import urljoin, urlparse
from validator_collection import checkers
from url_normalize import url_normalize


class UrlHandler:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.base_domain = self.get_url_domain(base_url)

    @staticmethod
    def get_base_url(url: str) -> str:
        parsed_url = urlparse(url)
        return f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"

    @staticmethod
    def get_url_domain(url: str) -> str:
        parsed_url = urlparse(url)
        return parsed_url.netloc.split(":")[0]

    def get_absolute_url(self, url: str) -> str:
        if self.is_url_belong_to_the_domain(url):
            return urljoin(self.base_url, url)
        return url

    def is_url_belong_to_the_domain(self, url: str) -> bool:
        url_domain = self.get_url_domain(url)
        return not url_domain or url_domain == self.base_domain

    @staticmethod
    def get_normalize_url(url: str) -> str:
        if url:
            parsed_url = urlparse(url)
            normalize_url = url_normalize(f"{parsed_url.scheme}://{parsed_url.netloc}/{parsed_url.path}")
            if parsed_url.fragment:
                normalize_url += f"#{parsed_url.fragment}"
            if parsed_url.query:
                url_query = parsed_url.query.replace('\\', '%5C')
                normalize_url += f"?{url_query}"
            return normalize_url
        return url

    @staticmethod
    def is_url(url: str) -> bool:
        return checkers.is_url(url)

    @staticmethod
    def is_article_url(url: str) -> bool:
        parsed_url = urlparse(url)
        url_path = parsed_url.path.split("/")
        if len(url_path) > 3:
            if url_path[-3] in ["post", "blog"] and url_path[-2].isdigit():
                return True
        return False

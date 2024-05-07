from urllib.parse import urlparse, parse_qs
from typing import List, Dict, Any
from .crypto import hmac_sha1


def create_sign_request_string(appid: str, secret: str, method: str, url: str, timestamp: int) -> str:
    pathname = get_url_pathname(url)
    sign_string = f"""
{appid}
{secret}
{timestamp}
{method}:{pathname}
"""
    return sign_string


def get_url_pathname(url: str) -> str:
    # If the URL does not start with 'http' or '//', prepend 'http://xxx.com'
    if not (url.startswith('http://') or url.startswith('https://') or url.startswith('//')):
        url = f"http://xxx.com{url}"

    # Normalize the URL in case it starts with '//'
    if url.startswith('//'):
        url = 'http:' + url

    # Parse the URL and extract the pathname
    parsed_url = urlparse(url)
    return f"/{parsed_url.path.lstrip('/')}"  # Ensure there is a leading slash


def sign_request(appid: str, secret: str, method: str, url: str, timestamp: int) -> str:
    sign_string = create_sign_request_string(appid, secret, method, url, timestamp)
    return hmac_sha1(sign_string, secret)

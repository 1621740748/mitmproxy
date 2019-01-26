"""
This script reflects all content passing through the proxy.
"""
from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    reflector = b"https://"
    flow.response.content = flow.response.content.replace(b"http://", reflector)
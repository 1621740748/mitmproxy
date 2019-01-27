"""
This script reflects all content passing through the proxy.
"""
from mitmproxy import http
import re

def response(flow: http.HTTPFlow) -> None:
    s=re.sub("http://([^\.]*)\.jrj\.com\.cn","https://\g<1>.jrj.com.cn",str(flow.response.content,"ISO-8859-1"))
    s=re.sub("http://([^\.]*)\.jrjimg\.cn","https://\g<1>.jrjimg.cn",s)
    flow.response.content = s.encode("ISO-8859-1")

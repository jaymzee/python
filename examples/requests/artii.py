"""
example using requests library

retreives ascii art for various fonts
"""

import requests
from requests.models import Response

def get_artii(text: str, **kwargs) -> Response:
    """ return an ascii art string """
    baseurl = 'http://artii.herokuapp.com/make'
    return requests.get(baseurl, dict(kwargs, text=text))


fonts = ['peaks', 'shadow', 'thick']

print(get_artii("default").text)
for font in fonts:
    print(get_artii(font, font=font).text)

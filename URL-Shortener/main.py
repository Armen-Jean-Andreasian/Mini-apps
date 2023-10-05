"""
pip install pyshorteners
"""
import pyshorteners


class URLShortener:
    def __init__(self):
        self.shortener = pyshorteners.Shortener()

    def shorten_url(self, long_url_local):
        short_url_local = self.shortener.tinyurl.short(long_url_local)
        return short_url_local


if __name__ == '__main__':
    url = input('Enter a URL:\n')

    url_shortener = URLShortener()
    shortened_url = url_shortener.shorten_url(url)

    print(f'Shortened URL: {shortened_url}')

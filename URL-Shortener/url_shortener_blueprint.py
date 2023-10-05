import random
import string


class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.short_code_length = 6  # Adjust the length as needed

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(self.short_code_length))

    def shorten_url(self, long_url):
        short_code = self.generate_short_code()
        self.url_mapping[short_code] = long_url
        return f'short.url/{short_code}'  # Replace 'short.url' with your desired domain

    def resolve_url(self, short_code):
        if short_code in self.url_mapping:
            return self.url_mapping[short_code]
        else:
            return None


if __name__ == '__main__':
    url_shortener = URLShortener()

    # Shorten a long URL
    long_url = 'https://www.example.com/very-long-url-that-needs-shortening'
    short_url = url_shortener.shorten_url(long_url)
    print(f'Shortened URL: https://www.{short_url}')

    # Resolve a short URL
    resolved_url = url_shortener.resolve_url(short_url.split('/')[-1])
    if resolved_url:
        print(f'Resolved URL: {resolved_url}')
    else:
        print('URL not found.')

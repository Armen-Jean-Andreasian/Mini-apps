"""
pip install requests, selenium

For this app I used State pattern, instead of Functional pattern.

"""
import requests
from selenium import webdriver
from file_manager import FileManager


class InstagramPhotoURL:
    PREFIX = "https://www.instagram.com/"
    ENDING = "media/?size=l"
    MAX_LENGTH = 40

    def __init__(self, url: str):
        self.url = url

    def url_length_check(self) -> None:
        if len(self.url) >= self.MAX_LENGTH:
            self.url = self.url[0:self.MAX_LENGTH]

    def url_validity_check(self):
        if self.url.startswith(self.PREFIX) and self.url.endswith('/'):
            self.url = self.url + self.ENDING
        else:
            print("Invalid URL. \nExample: https://www.instagram.com/p/BsOGulcndj-/\n")
            exit()


class Downloader(InstagramPhotoURL):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, '
                             'like Gecko Chrome/39.0.2171.95 Safari/537.36'}

    def access_url(self):
        """
        Accesses the url using Chrome browser to pass access check and get redirected.
        Updating self.url to a direct url to a file.
        """
        try:
            driver = webdriver.Chrome()
            driver.get(self.url)
            driver.refresh()

            self.url = driver.current_url
        except Exception:
            return "Couldn't access the url"

    def get_image(self):
        try:
            refreshed_response = requests.get(self.url, headers=self.HEADERS)

            image_bytes = refreshed_response.content
            FileManager.make_file(format_="jpg", file_data=image_bytes, name="image")
            print('Done!')

        except Exception:
            print(f"""You see this error because Streamlit couldn't handle the request again.
            So, you need to try to download the picture manually.
            Your link for manual downloading is:", {self.url}
            """)

    # def download(self):
    #     self.url_length_check()
    #     self.url_validity_check()
    #     self.access_url()
    #     self.get_image()


if __name__ == '__main__':
    URL = 'https://www.instagram.com/p/BsOGulcndj-/'

    downloader = Downloader(URL)
    downloader.url_length_check()
    downloader.url_validity_check()
    downloader.access_url()
    downloader.get_image()

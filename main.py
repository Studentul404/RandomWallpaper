import requests
import random
import sys
import ctypes
import os
from notify import notification

tag_string = ""
def main():
    tags = sys.argv[1:] or ["Wallpaper"]
    image_url = generate_image_url(tags)
    image_path = download_image(image_url)
    set_wallpaper(image_path)
    send_notification()


def generate_image_url(tags):
    global tag_string
    base_url = "https://source.unsplash.com/random/1920x1080/?"
    tag_string = random.choice(tags)
    return base_url + tag_string


def download_image(url):
    filename = "downloaded_image.jpg"
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    return os.path.abspath(filename)


def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)


def send_notification():
    message = f"Your wallpaper has been changed. It is a photo of {tag_string}. Enjoy!"
    notification.send(message)


if __name__ == "__main__":
    main()

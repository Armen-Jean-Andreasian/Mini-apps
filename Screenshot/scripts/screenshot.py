import time
import random
import pyautogui
import os


def generate_random_name(length: int) -> str:
    letters = "bcdfghjklaeioumnpqrstvwxyzaeiou"
    name = ""

    i = 0
    while i < length:
        name += random.choice(letters)
        i += 1
    return name


def take_screenshot():
    time.sleep(1)  # <-- Modify the delay

    folder_path = os.path.join(os.curdir, "../screenshots")
    os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

    filename = generate_random_name(7)
    file_path = os.path.join(folder_path, f'{filename}.png')

    pyautogui.screenshot(file_path)

    os.startfile(file_path)  # open picture
    os.system(f'explorer /select,"{file_path}"')  # open directory


if __name__ == '__main__':
    take_screenshot()

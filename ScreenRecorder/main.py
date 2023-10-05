import os
import cv2
import numpy as np
from PIL import ImageGrab
import random
import keyboard


class Recorder:
    fps = 30
    frame_size = (1920, 1080)

    @staticmethod
    def generate_random_name(length: int = None) -> str:
        if not length:
            length = 8
        letters = "bcdfghjklaeioumnpqrstvwxyzaeiou"
        name = ""

        i = 0
        while i < length:
            name += random.choice(letters)
            i += 1
        return name

    def __init__(self):
        self.filename = Recorder.generate_random_name() + '.mp4'
        self.folder_path = os.path.join(os.curdir, "../screenshots")

    @property
    def get_location(self):
        file_path = os.path.join(self.folder_path, self.filename)
        return file_path

    def record_screen(self):
        os.makedirs(self.folder_path, exist_ok=True)  # Create the folder if it doesn't exist

        # Try different codecs to find the best matching for potentially better quality
        """
        XVID : for mp4 videos
        MP4V : for mp4 videos
        """

        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        # Increase the bitrate for better quality
        out = cv2.VideoWriter(self.filename, fourcc, self.fps, self.frame_size, isColor=True)

        while True:
            img = ImageGrab.grab(bbox=(0, 0, self.frame_size[0], self.frame_size[1]))
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            out.write(frame)

            # Check for the 'Esc' key press to break the loop
            if keyboard.is_pressed('Esc'):
                break

        out.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    recorder = Recorder()
    recorder.record_screen()

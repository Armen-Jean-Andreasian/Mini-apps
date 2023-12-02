from PIL import Image, ImageSequence
from files import my_image, snow_animation


def add_snow_animation():
    animated_gif = Image.open(snow_animation)
    background = Image.open(my_image)

    background = background.convert("RGBA")

    frames = []
    for frame in ImageSequence.Iterator(animated_gif):
        frame = frame.resize(background.size)

        frame = frame.convert("RGBA")

        blended_frame = Image.blend(background, frame, alpha=0.5)

        frames.append(blended_frame)

    output_gif_path = 'output.gif'
    frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], duration=animated_gif.info['duration'],
                   loop=0)


if __name__ == '__main__':
    add_snow_animation()

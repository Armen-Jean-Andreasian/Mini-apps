from io import BytesIO
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random

vibrant_colors = ["#ec1254", "#f27c14", "#f5e31d", "#1ee8b6", "#26a1d5",
                  "#f7093b", "#f5cf1d", "#2cd27e", "#3ae5e7", "#9c1ae7",
                  "#570bb7", "#d042f8", "#2edbef", "#3aefb6", "#f10983",
                  "#0acb10", "#b8f331", "#fae534", "#fb9605", "#fc3d11",
                  "#ab20d9", "#2cc2d8", "#34e5b5", "#faf218", "#f534b3",
                  "#d61173", "#fb5cab", "#52c1fa", "#178bd5", "#f5ed16",
                  "#fb8318", "#fca53e", "#fe0557", "#2bcaf8", "#095fee",
                  "#fc123e", "#fddc23", "#21f0a9", "#1bd1f8", "#750ed5",
                  "#fc0c8e", "#fd8a1a", "#fde334", "#acfb13", "#21d1fd",
                  "#ee0f58", "#fb7a08", "#fdf12f", "#36e8f3", "#8b1df2",
                  "#0ce161", "#f84499", "#faf715", "#0ee2f5", "#8255df"]


def get_random_color(word, font_size, position, orientation, random_state=None, **kwargs):
    return random.choice(vibrant_colors)


def generate_wordcloud(text_input, bg_color="white"):
    # Split the input text into words
    words = text_input.split()

    # Determine image width and height based on the number of words
    num_words = len(words)
    width = min(800, num_words * 30)
    height = min(600, num_words * 20)

    wordcloud = WordCloud(
        background_color=bg_color, color_func=get_random_color,
        width=width, height=height
    ).generate(text_input)

    plt.figure(figsize=(width / 100, height / 100))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()

    # Convert the word cloud to a PIL Image object
    image = wordcloud.to_image()

    # Convert the PIL Image to bytes
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()

    with open('wordcloud.png', 'wb') as file:
        file.write(image_bytes)


if __name__ == "__main__":
    user_input = input("Enter the Text to be used for word cloud generation:\n")
    bg_choice = input('Choose the background color ("white" or "random"): ').lower()
    bg_color = 'white' if bg_choice == 'white' else random.choice(vibrant_colors)

    generate_wordcloud(user_input, bg_color)

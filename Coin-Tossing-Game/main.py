import os
import random


class Game:
    losing_coin_animation = "images/lose.gif"
    winning_coin_animation = "images/win.gif"
    coin = ["heads", "tails"]

    def __init__(self):
        self.score = {"user": 0, "AI": 0}

    def play(self, with_image=True):
        user_choice: str = input('Heads or Tails: ').strip().lower()
        if user_choice not in self.coin:
            return 'Wrong input! Try again!'
        else:
            flip: str = random.choice(self.coin)

            result = self.announce_results(result=flip, user_choice=user_choice)
            if with_image:
                self.display_image(result=result)

    @property
    def get_current_score(self) -> str:
        return f"You: {self.score['user']} vs AI: {self.score['AI']}\n"

    @classmethod
    def display_image(cls, result: bool) -> None:
        if result:
            image_file: str = cls.winning_coin_animation
        else:
            image_file: str = cls.losing_coin_animation

        os.system(f"start {image_file}")  # Open the image_file with the default viewer

    def announce_results(self, result: str, user_choice: str) -> bool:
        announcement = f"The coin landed on {result}."
        print(announcement)

        if result == user_choice:
            print("You won!")
            self.score["user"] += 1
            print(self.get_current_score)
            return True

        else:
            print("You lost!")
            self.score["AI"] += 1
            print(self.get_current_score)
            return False


if __name__ == '__main__':
    game = Game()
    while True:
        # set with_image=True to play with images
        game.play(with_image=False)

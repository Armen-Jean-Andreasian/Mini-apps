"""
Password-Generator Class

This module defines a simple Password-Generator class that generates random passwords
based on a set of characters including uppercase letters, lowercase letters, digits, and punctuation.


Usage:
1. Create an instance of Password-Generator.
    2. Optionally, set the desired password length using the set_length() method.
3. Generate a random password using the generate() method.
4. Retrieve the generated password using the get_result() method.
    5. Optionally, clear the generated password using the clear_result() method.

Example:
    generator = Password-Generator()
    generator.set_length(12)
    generator.generate()
    generated_password = generator.get_result()
    print(generated_password)

"""

import string
import random


class PasswordGenerator:
    LENGTH = 8

    def __init__(self):
        self.characters = (
                string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        )

        self._result = str()

    def generate(self):
        count = 0
        while count < self.LENGTH:
            self._result += random.choice(self.characters)
            count += 1

    def get_result(self):
        return self._result

    def clear_result(self):
        self._result = ''

    def set_length(self, length):
        self.LENGTH = length


if __name__ == '__main__':
    generator = PasswordGenerator()
    generator.set_length(12)
    generator.generate()
    print(generator.get_result())

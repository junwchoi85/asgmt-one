import os
import sys
import time


class Cli:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Cli, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def echo(self, message):
        print(message)

    def prompt(self, message, type_=str, default_=None):
        while True:
            try:
                user_input = input(message)
                if user_input == '' and default_ is not None:
                    return default_
                return type_(user_input)
            except ValueError:
                print(f"Invalid input. Please enter a valid {type_.__name__}.")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self, message="Press Enter to continue..."):
        input(message)

    def exit(self):
        print('Bye bye!')
        self.pause()
        sys.exit()

    def delay(self, seconds=2):
        print('Please wait...')
        time.sleep(seconds)

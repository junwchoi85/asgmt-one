import os

def clear_screen():
    """ Clear the screen """
    os.system('cls' if os.name == 'nt' else 'clear')
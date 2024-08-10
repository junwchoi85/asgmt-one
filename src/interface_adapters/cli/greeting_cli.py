import click
import os

def clear_screen():
    """ Clear the screen """
    os.system('cls' if os.name == 'nt' else 'clear')

@click.command()
def greet():
    """ Greet the user """
    clear_screen()
    click.echo(
        """
        *************************************************
        * Hello, welcome to the Car Rental System!      *
        * Please choose an option from the menu below:  *
        *                                               *
        * 1. Sign In                                    *
        * 2. Sign Up                                    *
        * 3. Exit                                       *
        *************************************************
        """)

    option = click.prompt('Input number ', type=int)
    while(option < 1 or option > 3):
        option = click.prompt('Invalid option. Please try again ', type=int)
    
    if option == 1:
        signIn()
    elif option == 2:
        signUp()
    elif option == 3:
        exit()

@click.command()
def signIn():
    """ Sign In """
    clear_screen()
    click.echo('Sign In')

@click.command()
def signUp():
    """ Sign Up """
    clear_screen()
    click.echo('Sign Up')

@click.command()
def exit():
    """ Exit """
    clear_screen()
    click.echo('Bye bye!')
    exit()

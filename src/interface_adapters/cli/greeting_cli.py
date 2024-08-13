import click

from interface_adapters.cli.clear_screen_cli import clear_screen
from interface_adapters.cli.sign_up_cli import signUp
# from interface_adapters.cli.sign_in_cli import signIn

@click.command()
@click.pass_context
def greet(ctx):
    """ Greet the user """
    user_controller = ctx.obj['user_controller']
    clear_screen()
    click.echo(
        """
        ============== Car Rental System ==============
         Hello, welcome to the Car Rental System!      
         Please choose an option from the menu below:  
                                                       
         1. Sign In                                    
         2. Sign Up                                    
         3. Exit                                       
        ===============================================
        """)

    option = click.prompt('Input number ', type=int)
    while(option < 1 or option > 3):
        option = click.prompt('Invalid option. Please try again ', type=int)
    
    if option == 1:
        click.echo('Sign In')
    elif option == 2:
        signUp(obj={'user_controller': user_controller})
    elif option == 3:
        exit_system()

@click.command()
def exit_system():
    """ Exit """
    # clear_screen()
    click.echo('Bye bye!')
    exit()

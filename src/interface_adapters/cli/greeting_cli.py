import click

from interface_adapters.cli.clear_screen_cli import clear_screen
from interface_adapters.cli.sign_up_cli import signUp
from interface_adapters.cli.sign_in_cli import signIn
from interface_adapters.cli.customer_sign_in_cli import customer_sign_in
from interface_adapters.cli.customer_sign_up_cli import customer_sign_up


@click.command()
@click.pass_context
def greet(ctx):
    """ Greet the user """
    customer_controller = ctx.obj['customer_controller']
    user_controller = ctx.obj['user_controller']
    ctx.obj['customer_controller'] = customer_controller
    ctx.obj['user_controller'] = user_controller

    clear_screen()
    click.echo(
        """
        ============== Car Rental System ==============
         Hello, welcome to the Car Rental System!      
         Please choose an option from the menu below:  
        
         1. Sign In
         2. Sign Up
         3. Exit
         4. Help
         5. Admin
        ===============================================
        """)

    option = click.prompt('Input number ', type=int)
    while (option < 1 or option > 5):
        option = click.prompt('Invalid option. Please try again ', type=int)

    if option == 1:
        customer_sign_in(obj={'customer_controller': customer_controller})
    elif option == 2:
        customer_sign_up(obj={'customer_controller': customer_controller})
        pass
    elif option == 3:
        exit_system()
    elif option == 4:
        click.echo("help")
    elif option == 5:
        signIn(obj={'user_controller': user_controller})


@click.command()
def exit_system():
    """ Exit """
    # clear_screen()
    click.echo('Bye bye!')
    exit()

import click
from interface_adapters.cli.clear_screen_cli import clear_screen
from interface_adapters.cli.customer_main_menu_cli import customer_main_menu

@click.command()
@click.pass_context
@click.option('--username', prompt='Your username', help='The user name')
@click.option('--password', prompt='Your password', help='The password')
def signIn(ctx, username, password):
    """ Sign In """
    # TODO : encrypt password
    clear_screen()
    click.echo('Sign In')
    
    user_controller = ctx.obj['user_controller']
    if not username or not password:
        click.echo('Username and password are required')
        return
    result = user_controller.sign_in(username=username, password=password)
    
    if result:
        click.echo('Sign in successful')
        customer_main_menu(obj = {'user': result})
    else:
        #TODO : Should go back to the main menu?
        click.echo('Invalid Username or Password')
        exit()

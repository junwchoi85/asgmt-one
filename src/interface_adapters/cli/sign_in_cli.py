import click
from interface_adapters.cli.clear_screen_cli import clear_screen
from interface_adapters.repositories.user_repository import UserRepository
from use_cases.user_use_case import UserUseCase
from entities.user import User

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

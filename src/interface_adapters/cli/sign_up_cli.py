import click
from frameworks_drivers.db_setup.database_setup import get_connection
from interface_adapters.cli.clear_screen_cli import clear_screen
from interface_adapters.repositories.user_repository import UserRepository
from use_cases.user_use_case import UserUseCase
from entities.user import User

@click.command()
@click.option('--username', prompt='Your username', help='The user name')
@click.option('--password', prompt='Your password', help='The password')
def signUp(username, password):
    """ Sign Up """
    clear_screen()
    click.echo('Sign Up')
    
    connection = get_connection()
    if connection is None:
        click.echo('Connection failed')
        return
    db_cursor = connection.cursor()

    #TODO: Implement error handling
    user_repository = UserRepository(db_cursor)
    create_user_use_case = UserUseCase(user_repository)

    result = create_user_use_case.createUser(username=username, password=password)

    click.echo('User created successfully') if result else click.echo('User creation failed')
    



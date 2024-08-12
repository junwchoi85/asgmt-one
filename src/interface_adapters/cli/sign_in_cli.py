import click
from frameworks_drivers.db_setup.database_setup import get_connection
from interface_adapters.cli.clear_screen_cli import clear_screen
from interface_adapters.repositories.user_repository import UserRepository
from use_cases.user_use_case import UserUseCase
from entities.user import User

@click.command()
@click.option('--username', prompt='Your username', help='The user name')
@click.option('--password', prompt='Your password', help='The password')
def signIn(username, password):
    """ Sign In """
    # TODO : encrypt password
    clear_screen()
    click.echo('Sign In')
    
    connection = get_connection()
    if connection is None:
        click.echo('Connection failed')
        return
    db_cursor = connection.cursor()

    user_repository = UserRepository(db_cursor)
    create_user_use_case = UserUseCase(user_repository)

    try:
        # TODO: 비밀번호 해시화
        result = create_user_use_case.signIn(username=username, password=password)
        if result:
            click.echo(f'Welcome {username}.')
        else:
            click.echo('Invalid username or password')
    except Exception as e:
        click.echo(f'An error occurred: {str(e)}')
    finally:
        # 트랜잭션 커밋
        connection.commit()
        connection.close()

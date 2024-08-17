import click
from interface_adapters.cli.clear_screen_cli import clear_screen
from interface_adapters.controllers.customer_controller import CustomerController

@click.command()
@click.pass_context
@click.option('--username', prompt='Your username', help='The user name')
@click.option('--password', prompt='Your password', help='The password')
def signUp(ctx, username, password):
    """ Sign Up """
    clear_screen()
    click.echo('Sign Up')
    
    # connection = get_connection()
    # if connection is None:
    #     click.echo('Connection failed')
    #     return
    # db_cursor = connection.cursor()

    # #TODO: Implement error handling
    # user_repository = UserRepository(db_cursor)
    # create_user_use_case = UserUseCase(user_repository)
    # Input validation
    customer_controller = ctx.obj['customer_controller']
    if not username or not password:
        click.echo('Username and password are required')
        return

    result = customer_controller.sign_up(username=username, password=password)

    click.echo('User created successfully') if result else click.echo('User creation failed')
    



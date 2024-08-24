import click

from interface_adapters.cli.manage_booking_cli import manage_booking
from interface_adapters.cli.manage_car_info_cli import manage_car_info


@click.command()
@click.pass_context
def user_main_menu(ctx):
    # ctx로 유저 정보를 받아온다.

    username = ctx.obj['username']

    """ User Main Menu """
    click.echo(f'Hello {username}, welcome to the MSE800 Car Rental System!')
    click.echo('Please choose an option from the menu below:')
    click.echo('1. Manage Car Information')
    click.echo('2. Manage booking')
    click.echo('3. Manage Customer')
    click.echo('4. Sign out')
    choice = click.prompt('\nChoose an option', type=int)

    while (choice < 1 or choice > 4):
        choice = click.prompt('Invalid option. Please try again ', type=int)
    if choice == 1:
        ctx.invoke(manage_car_info)
    elif choice == 2:
        ctx.invoke(manage_booking)
    elif choice == 3:
        click.echo('To be implemented')
    elif choice == 4:
        click.echo('Sign out')
        click.echo('Bye bye!')
        exit()

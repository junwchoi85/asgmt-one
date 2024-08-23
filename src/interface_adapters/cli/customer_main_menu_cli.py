import click

from interface_adapters.cli.car_list_cli import view_car_list
from interface_adapters.cli.view_customer_booking_cli import view_my_booking


@click.command()
@click.pass_context
def customer_main_menu(ctx):
    # ctx로 유저 정보를 받아온다.

    username = ctx.obj['username']
    click.echo(
        f'\nHello {username}, welcome to the MSE800 Car Rental System!')

    """ User Main Menu """

    click.echo('\nPlease choose an option from the menu below:')
    click.echo('1. View available cars')
    click.echo('2. Book a car')
    click.echo('3. View my bookings')
    click.echo('4. Sign out')
    choice = click.prompt('\nChoose an option', type=int)

    while (choice < 1 or choice > 4):
        choice = click.prompt(
            'Invalid option. Please try again ', type=int)
    if choice == 1:
        ctx.invoke(view_car_list)
    elif choice == 2:
        ctx.invoke(view_car_list)   # same as choice 1
    elif choice == 3:
        ctx.invoke(view_my_booking)
    elif choice == 4:
        click.echo('Sign out')
        click.pause('Bye bye!')
        exit()

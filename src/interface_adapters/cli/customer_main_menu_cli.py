import click

from interface_adapters.cli.car_list_cli import view_car_list


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
        # veiw_car_list(obj={'username': username, 'customer_controller': customer_controller})
    elif choice == 2:
        click.echo('Book a car')
    elif choice == 3:
        click.echo('View my bookings')
    elif choice == 4:
        click.echo('Sign out')
        click.pause('Bye bye!')
        exit()

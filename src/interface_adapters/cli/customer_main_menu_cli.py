import click


@click.command()
@click.pass_context
def customer_main_menu(ctx):
    # ctx로 유저 정보를 받아온다.

    username = ctx.obj['username']

    """ User Main Menu """
    click.echo(f'Hello {username}, welcome to the MSE800 Car Rental System!')
    click.echo('Please choose an option from the menu below:')
    click.echo('1. View available cars')
    click.echo('2. Book a car')
    click.echo('3. View my bookings')
    click.echo('4. Sign out')
    choice = click.prompt('\nChoose an option', type=int)

    while (choice < 1 or choice > 4):
        choice = click.prompt('Invalid option. Please try again ', type=int)
    if choice == 1:
        click.echo('View available cars')
    elif choice == 2:
        click.echo('Book a car')
    elif choice == 3:
        click.echo('View my bookings')
    elif choice == 4:
        click.echo('Sign out')

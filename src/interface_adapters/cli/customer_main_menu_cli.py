from interface_adapters.cli.car_list_cli import car_list
from interface_adapters.cli.cli import Cli
from interface_adapters.cli.view_customer_booking_cli import view_my_booking


def customer_main_menu(controllers: dict, credentials: dict, cli: Cli):
    cli.clear_screen()

    username = credentials['username']
    while True:
        cli.clear_screen()
        cli.echo(
            f'\nHello {username}, welcome to the MSE800 Car Rental System!')

        """ User Main Menu """

        cli.echo('\nPlease choose an option from the menu below:')
        cli.echo('1. View available cars')
        cli.echo('2. Book a car')
        cli.echo('3. View my bookings')
        cli.echo('4. Sign out')
        choice = cli.prompt('\nChoose an option: ', type_=int)

        while (choice < 1 or choice > 4):
            choice = cli.prompt(
                'Invalid option. Please try again. ', type_=int)
        if choice == 1:
            car_list(controllers, credentials, cli)
        elif choice == 2:
            car_list(controllers, credentials, cli)   # same as choice 1
        elif choice == 3:
            view_my_booking(controllers, credentials, cli)
        elif choice == 4:
            cli.echo('Sign out')
            cli.exit()

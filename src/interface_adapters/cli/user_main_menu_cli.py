from interface_adapters.cli.cli import Cli
from interface_adapters.cli.manage_booking_cli import manage_booking
from interface_adapters.cli.manage_car_info_cli import manage_car_info


def user_main_menu(controllers: dict, credentials: dict, cli: Cli):

    username = credentials['username']
    while True:
        cli.clear_screen()
        """ User Main Menu """
        cli.echo(f'Hello {username}, welcome to the MSE800 Car Rental System!')
        cli.echo('Please choose an option from the menu below:')
        cli.echo('1. Manage Car Information')
        cli.echo('2. Manage booking')
        cli.echo('3. Manage Customer')
        cli.echo('4. Sign out')
        choice = cli.prompt('\nChoose an option: ', type_=int)

        while (choice < 1 or choice > 4):
            choice = cli.prompt('Invalid option. Please try again ', type_=int)
        if choice == 1:
            manage_car_info(controllers, credentials, cli)
        elif choice == 2:
            manage_booking(controllers, credentials, cli)
        elif choice == 3:
            cli.echo('To be implemented')
            cli.pause()
        elif choice == 4:
            cli.echo('Sign out')
            cli.exit()

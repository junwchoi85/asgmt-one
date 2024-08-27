
from interface_adapters.cli.cli import Cli
from interface_adapters.cli.confirm_booking_cli import confirm_booking
from interface_adapters.cli.reject_booking_cli import reject_booking
from interface_adapters.cli.view_booking_cli import view_booking


def manage_booking(controllers: dict, credentials: dict, cli: Cli):
    while True:
        cli.clear_screen()
        cli.echo('======= Manage Booking =======\n')
        cli.echo('1. View Booking')
        cli.echo('2. Confirm Booking')
        cli.echo('3. Reject Booking')
        cli.echo('4. Exit')
        option = cli.prompt('Choose an option: ', type_=int)

        while (option < 1 or option > 4):
            option = cli.prompt('Invalid option. Please try again.', type_=int)

        if option == 1:
            view_booking(controllers, credentials, cli)
        elif option == 2:
            confirm_booking(controllers, credentials, cli)
        elif option == 3:
            reject_booking(controllers, credentials, cli)
        elif option == 4:
            return

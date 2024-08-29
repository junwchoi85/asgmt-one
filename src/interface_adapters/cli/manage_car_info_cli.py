from interface_adapters.cli.add_car_cli import add_car_info
from interface_adapters.cli.cli import Cli
from interface_adapters.cli.update_car_cli import update_car_info
from interface_adapters.cli.view_car_list_cli import view_car_list


def manage_car_info(controllers: dict, credentials: dict, cli: Cli):
    """ Manage Car Information Menu """
    cli.clear_screen()
    cli.echo('======= Manage Car Information =======\n')
    cli.echo('Please choose an option from the menu below:')
    cli.echo('1. View Car List')
    cli.echo('2. Add Car')
    cli.echo('3. Update Car Information')
    cli.echo('4. Exit')

    option = cli.prompt('\nChoose an option: ', type_=int)

    while (option < 1 or option > 3):
        option = cli.prompt('Invalid option. Please try again. ', type_=int)

    if option == 1:
        view_car_list(controllers, credentials, cli)
    elif option == 2:
        add_car_info(controllers, credentials, cli)
    elif option == 3:
        update_car_info(controllers, credentials, cli)
    elif option == 4:
        return

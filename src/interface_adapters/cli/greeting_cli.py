from interface_adapters.cli.cli import Cli
from interface_adapters.cli.help_cli import view_help
from interface_adapters.cli.sign_in_cli import signIn
from interface_adapters.cli.customer_sign_in_cli import customer_sign_in
from interface_adapters.cli.customer_sign_up_cli import customer_sign_up


def greet(controllers: dict, cli: Cli):
    """ Greet the user """
    # Retrieve controllers from tuple
    customer_controller = controllers['customer_controller']
    user_controller = controllers['user_controller']

    while True:
        cli.clear_screen()
        cli.echo(
            '''
============== Car Rental System ==============
Hello, welcome to the Car Rental System!      
Please choose an option from the menu below:  

1. Sign In
2. Sign Up
3. Exit
4. Help
5. Admin
===============================================
            ''')

        option = cli.prompt('Select an Option: ', type_=int)
        while (option < 1 or option > 5):
            option = cli.prompt('Invalid option. Please try again.', type_=int)

        if option == 1:
            customer_sign_in(controllers, cli)
        elif option == 2:
            customer_sign_up(controllers, cli)
            pass
        elif option == 3:
            cli.exit()
        elif option == 4:
            view_help(cli)
        elif option == 5:
            signIn(controllers, cli)

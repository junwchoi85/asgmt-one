from interface_adapters.cli.cli import Cli
from interface_adapters.cli.cli_util import is_success
from interface_adapters.cli.customer_main_menu_cli import customer_main_menu


def customer_sign_in(controllers: dict, cli: Cli):
    """ Sign In cli """
    cli.clear_screen()

    cli.echo('Sign In. Please enter your credentials')
    username = cli.prompt('Username: ')
    password = cli.prompt('Password: ')

    customer_controller = controllers['customer_controller']

    if not username or not password:
        cli.echo('Username and password are required')
        return
    req = {
        'username': username,
        'password': password
    }

    # singin
    res = customer_controller.sign_in(req)

    if is_success(res):
        cli.echo('Sign in successful')

        credentials = {
            'username': username,
            # 'password': password
        }
        customer_main_menu(controllers, credentials, cli)
    else:
        cli.echo(res['message'])
        cli.exit()
        return

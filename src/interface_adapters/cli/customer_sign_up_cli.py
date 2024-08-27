from interface_adapters.cli import cli
from interface_adapters.cli.cli_util import is_success
from interface_adapters.cli.customer_main_menu_cli import customer_main_menu


def customer_sign_up(controllers: dict, cli: cli.Cli):
    """ Sign Up """
    cli.clear_screen()
    # cli.echo('Sign Up')
    cli.echo('======= Sign Up =======')
    cli.echo('Please enter your credentials\n')
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

    # signup
    res = customer_controller.sign_up(req)

    if is_success(res):
        cli.echo('Sign up successful')
        credentials = {
            'username': username,
            # 'password': password
        }

        customer_main_menu(controllers, credentials, cli)
    else:
        cli.echo(res['message'])
        cli.exit()
        return

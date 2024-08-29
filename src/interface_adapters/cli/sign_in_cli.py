from interface_adapters.cli.cli import Cli
from interface_adapters.cli.cli_util import is_success
from interface_adapters.cli.user_main_menu_cli import user_main_menu


def signIn(controllers: dict, cli: Cli):
    """ Sign In """
    # TODO : encrypt password
    cli.clear_screen()
    cli.echo('======= Admin Sign In =======')
    cli.echo('Admin sign In. Please enter your credentials:\n')
    cli.echo(
        'If you are using the preloaded data, you can sign in with the following credentials:')
    cli.echo('Username: \'admin\'')
    cli.echo('Password: \'1234\'\n')
    username = cli.prompt('Username: ')
    password = cli.prompt('Password: ')

    user_controller = controllers['user_controller']
    if not username or not password:
        cli.echo('Username and password are required.')
        return
    req = {
        'username': username,
        'password': password
    }

    res = user_controller.sign_in(req)

    if is_success(res):
        cli.echo('Sign in successful.')
        credentials = {
            'username': username,
            # 'password': password
        }
        user_main_menu(controllers, credentials, cli)

    else:
        cli.echo(res['message'])
        cli.exit()
        return

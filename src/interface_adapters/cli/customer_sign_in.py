import click
from interface_adapters.cli.clear_screen_cli import clear_screen
from interface_adapters.cli.customer_main_menu_cli import customer_main_menu


@click.command()
@click.pass_context
@click.option('--username', prompt='Your username', help='The user name')
@click.option('--password', prompt='Your password', help='The password')
def customer_sign_in(ctx, username, password):
    """ Sign In """
    # TODO : encrypt password
    clear_screen()
    click.echo('Sign In')

    customer_controller = ctx.obj['customer_controller']
    if not username or not password:
        click.echo('Username and password are required')
        return
    req = {
        'username': username,
        'password': password
    }
    res = customer_controller.sign_in(req)

    if res['status'] == 'failure':
        click.echo(res['message'])
        click.pause('Bye bye!')
        return
    elif res['status'] == 'success':
        click.echo('Sign in successful')
        customer_main_menu(obj={'username': username,
                                'customer_controller': customer_controller})
    else:
        # TODO : Should go back to the main menu?
        click.echo('Invalid Username or Password')
        exit()

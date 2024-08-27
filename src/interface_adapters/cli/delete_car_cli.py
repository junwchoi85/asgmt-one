
from interface_adapters.cli.cli import Cli
from interface_adapters.cli.cli_util import is_success


def delete_car_info(user_controller, selected_car, cli: Cli):
    car = selected_car
    user_controller = ctx.obj['user_controller']
    cli.echo('Delete Car Information')
    cli.echo(f'Current Car Information: {car}')

    option = cli.prompt('Are you sure you want to delete this car? (y/n)')

    if option.lower() == 'y' or option.lower() == 'yes':
        req = {
            'car_id': car.car_id,
        }

        res = user_controller.delete_car_info(req)
        if is_success(res):
            cli.echo('Car deleted successfully')
            return
        else:
            cli.echo('Failed to delete car')
            cli.echo(res['message'])
            cli.pause(info='Press any key to continue...')
            return
    else:
        cli.echo('Car deletion cancelled')

import click

from interface_adapters.cli.cli_util import is_success


@click.command()
@click.pass_context
def delete_car_info(ctx):
    car = ctx.obj['car']
    user_controller = ctx.obj['user_controller']
    click.echo('Delete Car Information')
    click.echo(f'Current Car Information: {car}')

    option = click.prompt('Are you sure you want to delete this car? (y/n)')

    if option.lower() == 'y' or option.lower() == 'yes':
        req = {
            'car_id': car.car_id,
        }

        res = user_controller.delete_car_info(req)
        if is_success(res):
            click.echo('Car deleted successfully')
            ctx.invoke(ctx.parent.command)
        else:
            click.echo('Failed to delete car')
            click.echo(res['message'])
            click.pause(info='Press any key to continue...')
            ctx.invoke(ctx.parent.command)
    else:
        click.echo('Car deletion cancelled')

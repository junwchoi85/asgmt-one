import click

from interface_adapters.cli.cli_util import is_success


@click.command()
@click.pass_context
def update_car_info(ctx):
    car = ctx.obj['car']
    user_controller = ctx.obj['user_controller']
    click.echo('Update Car Information')
    click.echo(f'Current Car Information: {car}')

    click.echo('Please choose the information you want to update:')
    click.echo('1. Name')
    click.echo('2. Year')
    click.echo('3. Passenger')
    click.echo('4. Transmission')
    click.echo('5. Luggage Large')
    click.echo('6. Luggage Small')
    click.echo('7. Engine')
    click.echo('8. Fuel')

    option = click.prompt('...', type=int)

    req = {
        'car_id': car.car_id,
    }

    if option == 1:
        name = click.prompt('Name', default=car.name)
        req['name'] = name
    elif option == 2:
        year = click.prompt('Year', default=car.year)
        req['year'] = year
    elif option == 3:
        passenger = click.prompt('Passenger', default=car.passenger)
        req['passenger'] = passenger
    elif option == 4:
        transmission = click.prompt('Transmission', default=car.transmission)
        req['transmission'] = transmission
    elif option == 5:
        luggage_large = click.prompt(
            'Luggage Large', default=car.luggage_large)
        req['luggage_large'] = luggage_large
    elif option == 6:
        luggage_small = click.prompt(
            'Luggage Small', default=car.luggage_small)
        req['luggage_small'] = luggage_small
    elif option == 7:
        engine = click.prompt('Engine', default=car.engine)
        req['engine'] = engine
    elif option == 8:
        fuel = click.prompt('Fuel', default=car.fuel)
        req['fuel'] = fuel
    else:
        click.echo('Invalid option')

    res = user_controller.update_car_info(req)

    if is_success(res.statusCode):
        click.echo('Car information updated successfully')
        ctx.invoke(ctx.parent.command)
    else:
        click.echo('Failed to update car information')
        click.echo(res.message)
        click.pause(info='Press any key to continue...')
        ctx.invoke(ctx.parent.command)

import click

from interface_adapters.cli.cli_util import is_success


@click.command()
@click.pass_context
def add_car_info(ctx):
    user_controller = ctx.obj['user_controller']

    click.echo('Add Car Information')

    while True:
        click.echo('Please enter the information below:')

        name = click.prompt('Name')
        year = click.prompt('Year', type=int)
        passenger = click.prompt('Passenger', type=int)
        transmission = click.prompt('Transmission')
        luggage_large = click.prompt('Luggage Large', type=int)
        luggage_small = click.prompt('Luggage Small', type=int)
        engine = click.prompt('Engine')
        fuel = click.prompt('Fuel')
        price_per_day = click.prompt('Price per day', type=float)

        click.echo('\nPlease confirm the information below:')
        click.echo(f'Name: {name}')
        click.echo(f'Year: {year}')
        click.echo(f'Passenger: {passenger}')
        click.echo(f'Transmission: {transmission}')
        click.echo(f'Luggage Large: {luggage_large}')
        click.echo(f'Luggage Small: {luggage_small}')
        click.echo(f'Engine: {engine}')
        click.echo(f'Fuel: {fuel}')
        click.echo(f'Price per day: {price_per_day}')

        confirm = click.prompt('Is the information correct? (y/n)', type=str)
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            break

    req = {
        'name': name,
        'year': year,
        'passenger': passenger,
        'transmission': transmission,
        'luggage_large': luggage_large,
        'luggage_small': luggage_small,
        'engine': engine,
        'fuel': fuel,
        'price_per_day': price_per_day
    }

    res = user_controller.add_car_info(req)

    if is_success(res):
        click.echo('Car added successfully')
        click.pause(info='Press any key to continue...')
        ctx.invoke(ctx.parent.command)
    else:
        click.echo('Failed to add car')
        click.echo(res['message'])
        click.pause(info='Press any key to continue...')
        ctx.invoke(ctx.parent.command)

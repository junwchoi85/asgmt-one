from interface_adapters.cli.cli import Cli
from interface_adapters.cli.cli_util import is_success


def add_car_info(controllers: dict, credentials: dict, cli: Cli):
    user_controller = controllers['user_controller']

    cli.echo('Add Car Information')

    while True:
        cli.echo('Please enter the information below:')

        name = cli.prompt('Name')
        year = cli.prompt('Year', type_=int)
        passenger = cli.prompt('Passenger', type_=int)
        transmission = cli.prompt('Transmission')
        luggage_large = cli.prompt('Luggage Large', type_=int)
        luggage_small = cli.prompt('Luggage Small', type_=int)
        engine = cli.prompt('Engine')
        fuel = cli.prompt('Fuel')
        price_per_day = cli.prompt('Price per day', type_=float)

        cli.echo('\nPlease confirm the information below:')
        cli.echo(f'Name: {name}')
        cli.echo(f'Year: {year}')
        cli.echo(f'Passenger: {passenger}')
        cli.echo(f'Transmission: {transmission}')
        cli.echo(f'Luggage Large: {luggage_large}')
        cli.echo(f'Luggage Small: {luggage_small}')
        cli.echo(f'Engine: {engine}')
        cli.echo(f'Fuel: {fuel}')
        cli.echo(f'Price per day: {price_per_day}')

        confirm = cli.prompt('Is the information correct? (y/n)', type_=str)
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
        cli.echo('Car added successfully')
        cli.pause()
        return
    else:
        cli.echo('Failed to add car')
        cli.echo(res['message'])
        cli.pause()
        return

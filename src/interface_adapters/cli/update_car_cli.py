from interface_adapters.cli.cli import Cli
from interface_adapters.cli.cli_util import is_success


def update_car_info(user_controller, selected_car, cli: Cli):
    car = selected_car

    cli.echo('Update Car Information')
    cli.echo(f'Current Car Information: {car}')

    cli.echo('Please choose the information you want to update:')
    cli.echo('1. Name')
    cli.echo('2. Year')
    cli.echo('3. Passenger')
    cli.echo('4. Transmission')
    cli.echo('5. Luggage Large')
    cli.echo('6. Luggage Small')
    cli.echo('7. Engine')
    cli.echo('8. Fuel')

    option = cli.prompt('...', type_=int)

    req = {
        'car_id': car.car_id,
    }

    if option == 1:
        name = cli.prompt('Name', default=car.name)
        req['name'] = name
    elif option == 2:
        year = cli.prompt('Year', default=car.year)
        req['year'] = year
    elif option == 3:
        passenger = cli.prompt('Passenger', default=car.passenger)
        req['passenger'] = passenger
    elif option == 4:
        transmission = cli.prompt('Transmission', default=car.transmission)
        req['transmission'] = transmission
    elif option == 5:
        luggage_large = cli.prompt(
            'Luggage Large', default=car.luggage_large)
        req['luggage_large'] = luggage_large
    elif option == 6:
        luggage_small = cli.prompt(
            'Luggage Small', default=car.luggage_small)
        req['luggage_small'] = luggage_small
    elif option == 7:
        engine = cli.prompt('Engine', default=car.engine)
        req['engine'] = engine
    elif option == 8:
        fuel = cli.prompt('Fuel', default=car.fuel)
        req['fuel'] = fuel
    else:
        cli.echo('Invalid option')

    res = user_controller.update_car_info(req)

    if is_success(res.statusCode):
        cli.echo('Car information updated successfully')
        return
    else:
        cli.echo('Failed to update car information')
        cli.echo(res.message)
        cli.pause(info='Press any key to continue...')
        return

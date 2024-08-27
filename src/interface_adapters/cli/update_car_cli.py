from interface_adapters.cli.cli import Cli
from interface_adapters.cli.cli_util import is_success


def update_car_info(user_controller, selected_car, cli: Cli):
    car = selected_car
    cli.clear_screen()

    cli.echo('======= Update Car Information =======\n')
    cli.echo(
        f'You have selected: {car.name}, year: {
            car.year}, '
        f'passenger: {car.passenger}, '
        f'transmission: {car.transmission}, '
        f'luggage_large: {car.luggage_large}, '
        f'luggage_small: {car.luggage_small}, '
        f'engine: {car.engine}, '
        f'fuel: {car.fuel}, '
        f'price_per_day: {
            car.car_rental_terms.price_per_day}'
    )

    cli.echo('\nPlease choose the information you want to update:')
    cli.echo('To return to the previous menu, type \'0\'\n')
    cli.echo('1. Name')
    cli.echo('2. Year')
    cli.echo('3. Passenger')
    cli.echo('4. Transmission')
    cli.echo('5. Luggage Large')
    cli.echo('6. Luggage Small')
    cli.echo('7. Engine')
    cli.echo('8. Fuel')
    cli.echo('0. Return to previous menu')

    option = cli.prompt('\nChoose an option: ', type_=int)
    while (option < 0 or option > 8):
        option = cli.prompt('Invalid option. Please try again ', type_=int)

    req = {
        'car_id': car.car_id,
    }

    if option == 1:
        name = cli.prompt('Name: ', default_=car.name)
        req['name'] = name
    elif option == 2:
        year = cli.prompt('Year: ', default_=car.year)
        req['year'] = year
    elif option == 3:
        passenger = cli.prompt('Passenger: ', default_=car.passenger)
        req['passenger'] = passenger
    elif option == 4:
        transmission = cli.prompt(
            'Transmission: ', default_=car.transmission)
        req['transmission'] = transmission
    elif option == 5:
        luggage_large = cli.prompt(
            'Luggage Large: ', default_=car.luggage_large)
        req['luggage_large'] = luggage_large
    elif option == 6:
        luggage_small = cli.prompt(
            'Luggage Small: ', default_=car.luggage_small)
        req['luggage_small'] = luggage_small
    elif option == 7:
        engine = cli.prompt('Engine: ', default_=car.engine)
        req['engine'] = engine
    elif option == 8:
        fuel = cli.prompt('Fuel: ', default_=car.fuel)
        req['fuel'] = fuel
    elif option == 0:
        return
    else:
        cli.echo('Invalid option')

    res = user_controller.update_car_info(req)

    if is_success(res):
        cli.echo('Car information updated successfully')
        cli.pause()
        return
    else:
        cli.echo('Failed to update car information')
        cli.echo(res.message)
        cli.pause()
        return

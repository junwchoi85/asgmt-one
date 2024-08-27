
from interface_adapters.cli.cli import Cli
from interface_adapters.cli.cli_util import is_success


def delete_car_info(user_controller, selected_car, cli: Cli):
    car = selected_car
    cli.clear_screen()
    cli.echo('Delete Car Information')
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

    option = cli.prompt('Are you sure you want to delete this car? (y/n) ')

    if option.lower() == 'y' or option.lower() == 'yes':
        req = {
            'car_id': car.car_id,
        }

        res = user_controller.delete_car_info(req)
        if is_success(res):
            cli.echo('Car deleted successfully')
            cli.pause()
            return
        else:
            cli.echo('Failed to delete car')
            cli.echo(res['message'])
            cli.pause()
            return
    else:
        cli.echo('Car deletion cancelled')

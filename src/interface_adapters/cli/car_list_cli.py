from interface_adapters.cli.book_a_car_cli import book_a_car
from interface_adapters.cli.cli import Cli
from interface_adapters.cli.cli_util import is_success


def car_list(controllers: dict, credentials: dict, cli: Cli):

    customer_controller = controllers['customer_controller']
    username = credentials['username']

    page = 1
    page_size = 10

    while True:
        cli.echo('======= Available Cars =======')
        car_list = customer_controller.get_car_list_paged(
            page=page, page_size=page_size)
        if not car_list:
            cli.echo('No more cars available.')
            break

        cli.echo(f'\nPage {page}')
        for index, car in enumerate(car_list):
            cli.echo(
                f'{index+1}. name: {car.name}, year: {car.year}, '
                f'passenger: {car.passenger}, '
                f'transmission: {car.transmission}, '
                f'luggage_large: {car.luggage_large}, '
                f'luggage_small: {car.luggage_small}, '
                f'engine: {car.engine}, '
                f'fuel: {car.fuel}, '
                f'price_per_day: {car.car_rental_terms.price_per_day}'
            )

        cli.echo(
            '\nType in \'next\' to go to next page,\n or \'prev\' to go to previous page,\n or \'exit\' to exit. ')
        cli.echo(' or type in the number of the car to select.')
        action = cli.prompt('\nchoose option: ')
        # cli.echo(f'You have selected: {action}')

        if action.lower() == 'next':
            start = page * page_size
            end = start + page_size
            current_page_cars = car_list[start:end]

            if len(current_page_cars) < page_size:
                cli.pause(
                    'You are already on the final page. Press Enter to continue...')
                continue
            else:
                page += 1
        elif action.lower() == 'prev':
            if page > 1:
                page -= 1
            else:
                cli.pause(
                    'You are already on the first page. Press Enter to continue...')
        elif action.lower() == 'exit':
            # go back to previous cli.
            return
        # else if the user puts number
        elif action.isdigit():
            selected_index = int(action) - 1
            if selected_index < 0 or selected_index >= len(car_list):
                cli.echo('Invalid car number. Please try again.')
            else:
                selected_car = car_list[selected_index]
                cli.echo(
                    f'You have selected: {selected_car.name}, year: {
                        selected_car.year}, '
                    f'passenger: {selected_car.passenger}, transmission: {
                        selected_car.transmission}, '
                    f'luggage_large: {selected_car.luggage_large}, luggage_small: {
                        selected_car.luggage_small}, '
                    f'engine: {selected_car.engine}, fuel: {
                        selected_car.fuel}, '
                    f'price_per_day: {
                        selected_car.car_rental_terms.price_per_day}'
                )
                confirm = cli.prompt(
                    '\nconfirm booking? (yes/no): ', type_=str)
                if confirm == 'yes':
                    car_code = selected_car.car_code
                    car_rental_terms = selected_car.car_rental_terms

                    res = book_a_car(
                        customer_controller, username, car_code, car_rental_terms, cli)

                    if is_success(res):
                        cli.delay()
                        cli.echo(f'\n{res['message']}')
                        cli.pause('press any key to continue...')
                        # go back to parent menu.
                        return
                    else:
                        cli.delay()
                        cli.echo(f'\n{res['message']}')
                        cli.pause('press any key to continue...')
                        continue
        else:
            cli.echo(
                'Invalid option. Please enter "next", "prev", or "exit".')

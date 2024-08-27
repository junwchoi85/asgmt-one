from interface_adapters.cli.cli import Cli
from interface_adapters.cli.delete_car_cli import delete_car_info
from interface_adapters.cli.update_car_cli import update_car_info


def view_car_list(controllers: dict, credentials: dict, cli: Cli):
    cli.clear_screen()
    user_controller = controllers['user_controller']

    page = 1
    page_size = 10

    while True:
        car_list = user_controller.get_car_list_paged(
            page=page, page_size=page_size)
        if not car_list:
            cli.echo('No more cars available.')
            break

        cli.echo(f'\nPage {page} - Available Cars:')
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
        cli.echo('or type in the number of the car for management options.')
        action = cli.prompt('choose action: ')

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
            return

        # else if the user puts number
        elif action.isdigit():
            selected_index = int(action) - 1
            if selected_index < 0 or selected_index >= len(car_list):
                cli.echo('Invalid car number. Please try again.')
            else:
                cli.clear_screen()
                selected_car = car_list[selected_index]
                cli.echo(
                    f'You have selected: {selected_car.name}, year: {
                        selected_car.year}, '
                    f'passenger: {selected_car.passenger}, '
                    f'transmission: {selected_car.transmission}, '
                    f'luggage_large: {selected_car.luggage_large}, '
                    f'luggage_small: {selected_car.luggage_small}, '
                    f'engine: {selected_car.engine}, '
                    f'fuel: {selected_car.fuel}, '
                    f'price_per_day: {
                        selected_car.car_rental_terms.price_per_day}'
                )
                cli.echo('1. Update Car Information')
                cli.echo('2. Delete Car')
                cli.echo('3. Back')
                action = cli.prompt('choose action: ')
                if action == '1':
                    update_car_info(user_controller, selected_car, cli)
                    continue
                elif action == '2':
                    delete_car_info(user_controller, selected_car, cli)
                    continue
                elif action == '3':
                    continue
                else:
                    cli.echo('Invalid action. Please try again.')
        else:
            cli.echo('Invalid action. Please try again.')
            cli.pause('Press any key to continue...')
            continue

        cli.echo('Invalid action. Please try again.')
        continue

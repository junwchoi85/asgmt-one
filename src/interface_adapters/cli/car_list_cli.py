import click


@click.command()
@click.pass_context
def view_car_list(ctx):

    customer_controller = ctx.obj['customer_controller']

    page = 1
    page_size = 10

    while True:
        car_list = customer_controller.get_car_list_paged(
            page=page, page_size=page_size)
        if not car_list:
            click.echo('No more cars available.')
            break

        click.echo(f'\nPage {page} - Available Cars:')
        for index, car in enumerate(car_list):
            click.echo(f'{index+1}. name: {car.name}, year: {car.year}, passenger: {car.passenger}, transmission: {
                car.transmission}, luggage_large: {car.luggage_large}, luggage_small: {car.luggage_small}, engine: {car.engine}, fuel: {car.fuel}')

        click.echo(
            '\nType in \'next\' to go to next page,\n or \'prev\' to go to previous page,\n or \'exit\' to exit. ')
        click.echo('or type in the number of the car to select it.')
        action = click.prompt('choose action')
        # click.echo(f'You have selected: {action}')

        if action.lower() == 'next':
            if len(car_list) < page_size:
                click.echo('You are already on the final page.')
            else:
                page += 1
            page += 1
        elif action.lower() == 'prev':
            if page > 1:
                page -= 1
            else:
                click.echo('You are already on the first page.')
        elif action.lower() == 'exit':
            ctx.invoke(ctx.parent.command)
            break
        # else if the user puts number
        elif action.isdigit():
            selected_index = int(action) - 1
            if selected_index < 0 or selected_index >= len(car_list):
                click.echo('Invalid car number. Please try again.')
            else:
                selected_car = car_list[selected_index]
                click.echo(f'You have selected: {selected_car.name}, year: {selected_car.year}, passenger: {selected_car.passenger}, transmission: {selected_car.transmission}, luggage_large: {
                           selected_car.luggage_large}, luggage_small: {selected_car.luggage_small}, engine: {selected_car.engine}, fuel: {selected_car.fuel}')
                confirm = click.prompt('confirm booking? (yes/no)', type=str)
                if confirm == 'yes':
                    req = {
                        'username': ctx.obj['username'],
                        'car_code': selected_car.car_code,
                        'start_date': '2021-01-01',
                        'end_date': '2021-01-31',
                    }
                    customer_controller.make_a_booking(req)
                    # book the car
                    click.echo('Car booked!\n\n\n\n\n')
                    # go back to parent menu.
                    ctx.invoke(ctx.parent.command)
                    break
        else:
            click.echo(
                'Invalid option. Please enter "next", "prev", or "exit".')

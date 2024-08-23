import click


@click.command()
@click.pass_context
def manage_car_info(ctx):
    """ Manage Car Information Menu """
    click.echo('Please choose an option from the menu below:')
    click.echo('1. View Car List')
    click.echo('2. Add Car')
    click.echo('3. Update Car Information')
    click.echo('4. Exit')

    option = click.prompt('\nChoose an option', type=int)

    while (option < 1 or option > 3):
        option = click.prompt('Invalid option. Please try again ', type=int)

    if option == 1:
        ctx.invoke(view_car_list)
    elif option == 2:
        ctx.invoke(add_car)
    elif option == 3:
        ctx.invoke(update_car_info)
    elif option == 4:
        ctx.invoke(ctx.parent.command)


@click.command()
@click.pass_context
def view_car_list(ctx):
    user_controller = ctx.obj['user_controller']

    page = 1
    page_size = 10

    while True:
        car_list = user_controller.get_car_list_paged(
            page=page, page_size=page_size)
        if not car_list:
            click.echo('No more cars available.')
            break

        click.echo(f'\nPage {page} - Available Cars:')
        for index, car in enumerate(car_list):
            click.echo(
                f'{index+1}. name: {car.name}, year: {car.year}, '
                f'passenger: {car.passenger}, '
                f'transmission: {car.transmission}, '
                f'luggage_large: {car.luggage_large}, '
                f'luggage_small: {car.luggage_small}, '
                f'engine: {car.engine}, '
                f'fuel: {car.fuel}, '
                f'price_per_day: {car.car_rental_terms.price_per_day}'
            )

        click.echo(
            '\nType in \'next\' to go to next page,\n or \'prev\' to go to previous page,\n or \'exit\' to exit. ')
        click.echo('or type in the number of the car for management options.')
        action = click.prompt('choose action')

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
                click.echo(
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
                click.echo('1. Update Car Information')
                click.echo('2. Delete Car')
                click.echo('3. Back')
                action = click.prompt('choose action')
                if action == '1':
                    ctx.invoke(update_car_info, car=selected_car)
                elif action == '2':
                    ctx.invoke(delete_car, car=selected_car)
                elif action == '3':
                    continue
                else:
                    click.echo('Invalid action. Please try again.')
        else:
            click.echo('Invalid action. Please try again.')
            continue

        click.echo('Invalid action. Please try again.')
        continue

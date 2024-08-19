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

        click.prompt(
            '\nType in \'next\' to go to next page,\n or \'prev\' to go to previous page,\n or \'exit\' to exit. ', type=str)
        action = click.prompt('choose action', type=str)
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
        else:
            click.echo(
                'Invalid option. Please enter "next", "prev", or "exit".')

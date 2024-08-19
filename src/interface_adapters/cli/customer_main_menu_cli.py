import click


@click.command()
@click.pass_context
def customer_main_menu(ctx):
    # ctx로 유저 정보를 받아온다.

    username = ctx.obj['username']
    customer_controller = ctx.obj['customer_controller']
    click.echo(
        f'Hello {username}, welcome to the MSE800 Car Rental System!')

    while True:
        """ User Main Menu """

        click.echo('\nPlease choose an option from the menu below:')
        click.echo('1. View available cars')
        click.echo('2. Book a car')
        click.echo('3. View my bookings')
        click.echo('4. Sign out')
        choice = click.prompt('\nChoose an option', type=int)

        while (choice < 1 or choice > 4):
            choice = click.prompt(
                'Invalid option. Please try again ', type=int)
        if choice == 1:
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

                next_page = click.prompt(
                    'Do you want to see the next page? (yes/no)', type=str)
                if next_page.lower() != 'yes':
                    break
                page += 1
        elif choice == 2:
            click.echo('Book a car')
        elif choice == 3:
            click.echo('View my bookings')
        elif choice == 4:
            click.echo('Sign out')
            click.echo('Bye bye!')
            exit()

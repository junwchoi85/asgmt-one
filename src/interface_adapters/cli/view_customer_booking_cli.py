import click

from interface_adapters.cli.cli_util import is_success


@click.command()
@click.pass_context
def view_my_booking(ctx):
    """ View customer's bookings """
    customer_controller = ctx.obj['customer_controller']
    username = ctx.obj['username']

    req = {
        'username': username
    }
    booking_details = customer_controller.get_booking_list(req)  # 여기

    if not booking_details:
        click.echo('You have no bookings.')
        return

    click.echo('\nYour Bookings:')
    for index, booking_detail in enumerate(booking_details):
        click.echo(
            f'{index+1}. Car: {booking_detail.name}, '
            f'from: {booking_detail.start_date}, to: {
                booking_detail.end_date}, '
            f'price: {booking_detail.total_fee}'
            f'status: {booking_detail.status}'
        )

    click.pause('\nPress any key to return to previous menu.')
    click.clear()
    # return to previous menu
    ctx.invoke(ctx.parent.command)

    # TODO : For future implementation
    # click.echo('\nType in the number of the booking to view details.')
    # click.echo('or type in \'exit\' to exit.')
    # action = click.prompt('choose action')

    # if action.lower() == 'exit':
    #     return

    # if action.isdigit():
    #     selected_index = int(action) - 1
    #     if selected_index < 0 or selected_index >= len(booking_details):
    #         click.echo('Invalid booking number. Please try again.')
    #     else:
    #         booking_detail = booking_details[selected_index]
    #         click.echo(
    #             f'Car: {booking_detail.car.name}, '
    #             f'from: {booking_detail.start_date}, to: {
    #                 booking_detail.end_date}, '
    #             f'price: {booking_detail.price}'
    #         )
    #         click.echo('Type in \'cancel\' to cancel the booking.')
    #         action = click.prompt('choose action')
    #         if action.lower() == 'cancel':
    #             is_success(customer_controller.cancel_booking(
    #                 booking_detail.id))
    #             return

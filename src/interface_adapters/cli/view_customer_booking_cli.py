
from interface_adapters.cli.cli import Cli
from interface_adapters.cli.cli_util import is_success


def view_my_booking(controllers: dict, credentials: dict, cli: Cli):
    """ View customer's bookings """
    customer_controller = controllers['customer_controller']
    username = credentials['username']

    cli.clear_screen()
    cli.echo('======= View My Bookings =======')

    req = {
        'username': username
    }
    booking_details = customer_controller.get_booking_list(req)  # 여기

    if not booking_details:
        cli.echo('You have no bookings.')
        cli.pause()
        return

    cli.echo('\nYour Bookings:')
    for index, booking_detail in enumerate(booking_details):
        cli.echo(
            f'{index+1}. Car: {booking_detail.name}, '
            f'from: {booking_detail.start_date}, to: {
                booking_detail.end_date}, '
            f'price: {booking_detail.total_fee}'
            f'status: {booking_detail.status}'
        )

    cli.pause('\nPress any key to return to previous menu.')
    # return to previous menu
    return

    # TODO : For future implementation
    # cli.echo('\nType in the number of the booking to view details.')
    # cli.echo('or type in \'exit\' to exit.')
    # action = cli.prompt('choose action')

    # if action.lower() == 'exit':
    #     return

    # if action.isdigit():
    #     selected_index = int(action) - 1
    #     if selected_index < 0 or selected_index >= len(booking_details):
    #         cli.echo('Invalid booking number. Please try again.')
    #     else:
    #         booking_detail = booking_details[selected_index]
    #         cli.echo(
    #             f'Car: {booking_detail.car.name}, '
    #             f'from: {booking_detail.start_date}, to: {
    #                 booking_detail.end_date}, '
    #             f'price: {booking_detail.price}'
    #         )
    #         cli.echo('Type in \'cancel\' to cancel the booking.')
    #         action = cli.prompt('choose action')
    #         if action.lower() == 'cancel':
    #             is_success(customer_controller.cancel_booking(
    #                 booking_detail.id))
    #             return

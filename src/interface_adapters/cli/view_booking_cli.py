from interface_adapters.cli.cli import Cli


def view_booking(controllers: dict, credentials: dict, cli: Cli):
    user_controller = controllers['user_controller']

    req = {
        'status': None
    }
    res = user_controller.get_booking_list(req)
    booking_list = res['booking_list']
    cli.echo('\nBooking List:')
    for index, booking in enumerate(booking_list):
        # print(type(booking))
        cli.echo(f'{index+1}Booking ID: {booking.booking_id}, Customer ID: {booking.cst_id}, Car Detail ID: {booking.car_dtl_id}, Start Date: {
            booking.start_date}, End Date: {booking.end_date}, Total Fee: {booking.total_fee}, Status: {booking.status}')

    cli.pause('Press any key to continue')

    return

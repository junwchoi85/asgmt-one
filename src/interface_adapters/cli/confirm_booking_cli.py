from interface_adapters.cli.cli import Cli


def confirm_booking(controllers: dict, credentials: dict, cli: Cli):
    user_controller = controllers['user_controller']

    cli.clear_screen()
    cli.echo('======= Confirm Booking =======\n')

    req = {
        'status': 'reserved'
    }
    res = user_controller.get_booking_list(req)
    booking_list = res['booking_list']
    cli.echo('\nBooking List:')
    for index, booking in enumerate(booking_list):
        # print(type(booking))
        cli.echo(f'{index+1}. Booking ID: {booking.booking_id}, Customer ID: {booking.cst_id}, Car Detail ID: {booking.car_dtl_id}, Start Date: {
            booking.start_date}, End Date: {booking.end_date}, Total Fee: {booking.total_fee}, Status: {booking.status}')

    while True:
        cli.echo(
            '\nType in the number of the booking to confirm it, or type \'exit\' to exit.')

        action = cli.prompt('choose an option: ')
        if action.lower() == 'exit':
            # return to previous menu
            return

        elif action.isdigit():
            pass
            selected_index = int(action) - 1
            if selected_index < 0 or selected_index >= len(booking_list):
                cli.echo('Invalid booking number. Please try again.')
            else:
                selected_booking = booking_list[selected_index]
                cli.echo(f'\nYou have selected: {selected_booking.booking_id}, Customer ID: {selected_booking.cst_id}, Car Detail ID: {selected_booking.car_dtl_id}, Start Date: {
                    selected_booking.start_date}, End Date: {selected_booking.end_date}, Total Fee: {selected_booking.total_fee}, Status: {selected_booking.status}')
                confirm = cli.prompt(
                    'confirm booking? (yes/no): ', type_=str)
                if confirm == 'yes':
                    req = {
                        'booking_id': selected_booking.booking_id,
                        'status': 'confirmed'
                    }
                    user_controller.confirm_booking(req)
                    # book the car
                    cli.delay()
                    cli.echo('Booking confirmed!\n\n\n\n\n')
                    cli.pause('Press any key to continue')
                    return

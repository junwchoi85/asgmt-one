import click


@click.command()
@click.pass_context
def manage_booking(ctx):

    click.echo('\nManage Booking:')
    click.echo('1. View Booking')
    click.echo('2. Confirm Booking')
    click.echo('3. Reject Booking')
    click.echo('4. Exit')
    option = click.prompt('Choose an option', type=int)

    while (option < 1 or option > 4):
        option = click.prompt('Invalid option. Please try again ', type=int)

    if option == 1:
        ctx.invoke(view_booking)
    elif option == 2:
        ctx.invoke(confirm_booking)
    elif option == 3:
        ctx.invoke(reject_booking)


@click.command()
@click.pass_context
def reject_booking(ctx):
    user_controller = ctx.obj['user_controller']

    req = {
        'booking_status': 'reserved'
    }
    res = user_controller.get_booking_list(req)
    booking_list = res['booking_list']
    click.echo('\nBooking List:')
    for index, booking in enumerate(booking_list):
        # print(type(booking))
        click.echo(f'{index+1}. Booking ID: {booking.booking_id}, Customer ID: {booking.cst_id}, Car Detail ID: {booking.car_dtl_id}, Start Date: {
            booking.start_date}, End Date: {booking.end_date}, Total Fee: {booking.total_fee}, Status: {booking.status}')

    while True:
        action = click.prompt(
            'Type in the number of the booking to reject it, or type \'exit\' to exit.')
        if action.lower() == 'exit':
            # return to previous menu
            ctx.invoke(ctx.parent.command)
            break
        elif action.isdigit():
            selected_index = int(action) - 1
            if selected_index < 0 or selected_index >= len(booking_list):
                click.echo('Invalid booking number. Please try again.')
            else:
                selected_booking = booking_list[selected_index]
                click.echo(f'You have selected: {selected_booking.booking_id}, Customer ID: {selected_booking.cst_id}, Car Detail ID: {selected_booking.car_dtl_id}, Start Date: {
                    selected_booking.start_date}, End Date: {selected_booking.end_date}, Total Fee: {selected_booking.total_fee}, Status: {selected_booking.status}')
                confirm = click.prompt(
                    'reject booking? (yes/no)', type=str)
                if confirm == 'yes':
                    req = {
                        'booking_id': selected_booking.booking_id,
                        'status': 'rejected'
                    }
                    user_controller.reject_booking(req)
                    # book the car
                    click.echo('Booking rejected!\n\n\n\n\n')
                    click.pause('Press any key to continue')
                    ctx.invoke(ctx.parent.command)
                    break


@click.command()
@click.pass_context
def confirm_booking(ctx):
    user_controller = ctx.obj['user_controller']

    req = {
        'status': 'reserved'
    }
    res = user_controller.get_booking_list(req)
    booking_list = res['booking_list']
    click.echo('\nBooking List:')
    for index, booking in enumerate(booking_list):
        # print(type(booking))
        click.echo(f'{index+1}. Booking ID: {booking.booking_id}, Customer ID: {booking.cst_id}, Car Detail ID: {booking.car_dtl_id}, Start Date: {
            booking.start_date}, End Date: {booking.end_date}, Total Fee: {booking.total_fee}, Status: {booking.status}')

    while True:
        action = click.prompt(
            'Type in the number of the booking to confirm it, or type \'exit\' to exit.')
        if action.lower() == 'exit':
            # return to previous menu
            ctx.invoke(ctx.parent.command)
            break
        elif action.isdigit():
            pass
            selected_index = int(action) - 1
            if selected_index < 0 or selected_index >= len(booking_list):
                click.echo('Invalid booking number. Please try again.')
            else:
                selected_booking = booking_list[selected_index]
                click.echo(f'You have selected: {selected_booking.booking_id}, Customer ID: {selected_booking.cst_id}, Car Detail ID: {selected_booking.car_dtl_id}, Start Date: {
                    selected_booking.start_date}, End Date: {selected_booking.end_date}, Total Fee: {selected_booking.total_fee}, Status: {selected_booking.status}')
                confirm = click.prompt(
                    'confirm booking? (yes/no)', type=str)
                if confirm == 'yes':
                    req = {
                        'booking_id': selected_booking.booking_id,
                        'status': 'confirmed'
                    }
                    user_controller.confirm_booking(req)
                    # book the car
                    click.echo('Booking confirmed!\n\n\n\n\n')
                    click.pause('Press any key to continue')
                    ctx.invoke(ctx.parent.command)
                    break


@click.command()
@click.pass_context
def view_booking(ctx):
    user_controller = ctx.obj['user_controller']

    req = {
        'status': None
    }
    res = user_controller.get_booking_list(req)
    booking_list = res['booking_list']
    click.echo('\nBooking List:')
    for booking in booking_list:
        # print(type(booking))
        click.echo(f'Booking ID: {booking.booking_id}, Customer ID: {booking.cst_id}, Car Detail ID: {booking.car_dtl_id}, Start Date: {
            booking.start_date}, End Date: {booking.end_date}, Total Fee: {booking.total_fee}, Status: {booking.status}')

    click.pause('Press any key to continue')

    ctx.invoke(ctx.parent.command)

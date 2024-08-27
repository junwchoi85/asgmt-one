from interface_adapters.cli.cli import Cli


def book_a_car(customer_controller, username, car_code, car_rental_terms, cli: Cli):
    cli.echo('\n\nFrom when would you like to book the car?')
    start_date = cli.prompt(
        'Start Date (YYYY-MM-DD): ', type_=str)
    cli.echo('\nUntil when would you like to book the car?')
    end_date = cli.prompt('End Date (YYYY-MM-DD): ', type_=str)

    req = {
        'username': username,
        'car_code': car_code,
        'start_date': start_date,
        'end_date': end_date,
        'rental_terms': car_rental_terms
    }
    return customer_controller.make_a_booking(req)

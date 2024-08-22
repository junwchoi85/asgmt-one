
# import pytest

# from interface_adapters.repositories.booking_repository import BookingRepository
# from interface_adapters.repositories.car_repository import CarRepository
# from interface_adapters.repositories.customer_repository import CustomerRepository
# from use_cases.customer_use_case import CustomerUseCase
# import datetime

# from use_cases.user_use_case import UserUseCase
# from utils import date_utils


# PASSWORD = 'password'


# def test_book_car(customer_repo, car_repo, booking_repo, transaction_manager, test_logger):
#     # Setup
#     customer_use_case = CustomerUseCase(customer_repo,
#                                         car_repo,
#                                         booking_repo,
#                                         transaction_manager)
#     """
#     Book a car as a customer
#     """
#     username = 'test_booking'

#     # Create a customer
#     req_create_customer = {
#         'username': username,
#         'password': PASSWORD
#     }
#     rslt_create_customer = customer_use_case.sign_up(req_create_customer)
#     # get the customer
#     # test_logger.debug(customer.cst_id)
#     # Select a Car
#     cars = customer_use_case.get_car_list()
#     # select the first car
#     car_selected = cars[0]

#     # Get today's date
#     today = datetime.date.today()
#     one_month_from_today = today + datetime.timedelta(days=30)
#     # Format today's date as 'YYYY-MM-DD'
#     today_formatted = today.strftime('%Y-%m-%d')
#     one_month_from_today_formatted = one_month_from_today.strftime('%Y-%m-%d')
#     # Book the car
#     req_book_car = {
#         'username': username,
#         'car_code': car_selected.car_code,
#         'start_date': today_formatted,
#         'end_date': one_month_from_today_formatted,
#     }
#     # Test
#     rewult = customer_use_case.make_a_booking(req_book_car)
#     # Verify
#     assert rewult is not None


# def test_get_booking_info(user_repo,
#                           booking_repo,
#                           customer_repo,
#                           car_repo,
#                           transaction_manager, test_logger):
#     """
#     Test get_booking_info
#     """
#     # Setup
#     customer_use_case = CustomerUseCase(customer_repo,
#                                         car_repo,
#                                         booking_repo,
#                                         transaction_manager)
#     user_use_case = UserUseCase(
#         user_repo, booking_repo, car_repo, transaction_manager)

#     username = 'test_get_booking_info'
#     # Setup
#     # 1. Create a customer
#     req_create_customer = {
#         'username': username,
#         'password': PASSWORD
#     }
#     rslt_create_customer = customer_use_case.sign_up(req_create_customer)
#     # 2. Select a Car
#     cars = customer_use_case.get_car_list()
#     car_selected = cars[0]

#     # 3. Book the car
#     req_book_car = {
#         'username': username,
#         'car_code': car_selected.car_code,
#         'start_date': date_utils.get_today_formatted(),
#         'end_date': date_utils.get_one_month_from_today_formatted(),
#     }
#     res_book_car = customer_use_case.make_a_booking(req_book_car)

#     user_use_case = UserUseCase(
#         user_repo, booking_repo, car_repo, transaction_manager)

#     # Test
#     req = {
#         'status': 'reserved'
#     }

#     booking_list = user_use_case.get_booking_list(req)
#     # test_logger.debug('***************')
#     # test_logger.debug(booking_list)
#     # test_logger.debug('***************')

#     # Verify
#     assert booking_list is not None
#     assert len(booking_list) > 0
#     assert booking_list[0].status == 'reserved'


# def test_confirm_booking(user_repo,
#                          booking_repo,
#                          customer_repo,
#                          car_repo,
#                          transaction_manager, test_logger):
#     # Setup
#     customer_use_case = CustomerUseCase(customer_repo,
#                                         car_repo,
#                                         booking_repo,
#                                         transaction_manager)
#     user_use_case = UserUseCase(
#         user_repo, booking_repo, car_repo, transaction_manager)

#     username = 'test_confirm_booking'
#     # Setup
#     # 1. Create a customer
#     req_create_customer = {
#         'username': username,
#         'password': PASSWORD
#     }
#     rslt_create_customer = customer_use_case.sign_up(req_create_customer)
#     # 2. Select a Car
#     cars = customer_use_case.get_car_list()
#     car_selected = cars[0]

#     # 3. Book the car
#     req_book_car = {
#         'username': username,
#         'car_code': car_selected.car_code,
#         'start_date': date_utils.get_today_formatted(),
#         'end_date': date_utils.get_one_month_from_today_formatted(),
#     }
#     res_book_car = customer_use_case.make_a_booking(req_book_car)

#     # Test
#     user_use_case = UserUseCase(
#         user_repo, booking_repo, car_repo, transaction_manager)

#     req = {
#         'status': 'reserved'
#     }

#     booking_list = user_use_case.get_booking_list(req)

#     # Confirm the booking
#     req_confirm_booking = {
#         'booking_id': booking_list[0].booking_id,
#         'status': 'confirmed'
#     }

#     user_use_case.confirm_booking(req_confirm_booking)

#     # Get the booking info
#     req = {
#         'status': 'confirmed'
#     }
#     booking_list = user_use_case.get_booking_list(req)

#     # Verify
#     assert booking_list is not None
#     assert len(booking_list) > 0
#     assert booking_list[0].status == 'confirmed'

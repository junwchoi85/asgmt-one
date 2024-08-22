from use_cases.user_use_case import UserUseCase
from entities.user import User


def test_create_user(user_repo):
    pass


def test_create_user_fail(user_repo):
    pass


def test_sign_in(user_repo,
                 booking_repo,
                 car_repo,
                 transaction_manager):
    # Setup
    user_use_case = UserUseCase(
        user_repo, booking_repo, car_repo, transaction_manager)

    req = {
        'username': 'test',
        'password': 'test'
    }
    # Save the user
    new_user = user_use_case.sign_up(req)
    # Test
    result = user_use_case.sign_in(req)
    # Verify
    assert result is not None
    assert result.username == req['username']

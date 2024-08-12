import pytest
from interface_adapters.repositories.user_repository import UserRepository
from use_cases.user_use_case import UserUseCase
from entities.user import User

@pytest.fixture
def user_repo(db_cursor):
    return UserRepository(db_cursor)

def test_create_user(user_repo):
    # Setup
    user_use_case = UserUseCase(user_repo)
    # Create a user
    user = User(
        user_id = None, 
        user_code = None,
        username = 'username@test.com', 
        password = 'userpassword'
    )
    # Test
    result = user_use_case.createUser(user)

    # Verify
    assert result == True
    
    # Verify user is in the database
    user_from_db = user_repo.get_by_username('test')
    assert user_from_db is not None
    assert user_from_db.username == 'test'

def test_create_user_fail(user_repo):
    #TODO: Implement
    pass

def test_sign_in(user_repo):
    # Setup
    user_use_case = UserUseCase(user_repo)
    # Create a user
    user = User(
        user_id = None, 
        user_code = None,
        username = 'username@test.com', 
        password = 'userpassword'
    )
    # Save the user
    user_repo.save(user)
    # Test
    result = user_use_case.signIn(user.username, user.password)
    # Verify
    assert result is not None
    assert result.username == user.username

if __name__ == '__main__':
    pytest.main(['-s', __file__])


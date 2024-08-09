import pytest
from adapters.repositories.user_repository import UserRepository
from use_cases.user_use_case import CreateUser
from entities.user import User

@pytest.fixture
def user_repo(db_cursor):
    return UserRepository(db_cursor)

def test_create_user(user_repo):
    # Setup
    user_use_case = CreateUser(user_repo)
    # Create a user
    user = User(
        user_id=4, 
        user_code='003', 
        username='test', 
        password='test'
    )
    # Test
    result = user_use_case.execute(user)

    # Verify
    assert result == True
    
    # Verify user is in the database
    user_from_db = user_repo.get_by_username('test')
    assert user_from_db is not None
    assert user_from_db.username == 'test'
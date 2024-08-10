import pytest
import sqlite3
from frameworks_drivers.db_setup.database_setup import setup_database

@pytest.fixture(scope='session')
def connection():
    # 세션 범위의 인메모리 SQLite 데이터베이스 생성
    conn = sqlite3.connect(':memory:')
    yield conn
    conn.close()

@pytest.fixture(scope='session')
def setup_database_fixture(connection):
    # 세션 범위에서 테이블 생성
    setup_database()
    yield
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS user;')
    cursor.execute('DROP TABLE IF EXISTS role;')
    cursor.execute('DROP TABLE IF EXISTS user_role;')
    cursor.execute('DROP TABLE IF EXISTS car;')
    cursor.execute('DROP TABLE IF EXISTS booking;')
    connection.commit()

@pytest.fixture(scope='function')
def db_cursor(connection, setup_database_fixture):
    # 각 테스트 함수마다 새로운 커서 생성
    cursor = connection.cursor()
    yield cursor
    cursor.close()
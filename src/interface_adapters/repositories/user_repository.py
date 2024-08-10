from frameworks_drivers.db_setup.database_setup import get_connection
from entities.user import User

class UserRepository:
    def __init__(self, db_cursor):
        self.db_cursor = db_cursor

    def save(self, user: User) -> bool:
        """
        Save a user to the database
        :param user: User object
        :return: None
        """
        try:
            conn = get_connection()
            c = conn.cursor()
            c.execute(
                '''
                INSERT INTO user (user_id, user_code, username, password)
                VALUES (?, ?, ?, ?)
                ''',
                (user.user_id, user.user_code, user.username, user.password))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            return False
    
    def get_last_user_code(seff) -> str:
        """
        Get the last user code
        :return: User code
        """
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            '''
            SELECT user_code FROM user ORDER BY user_id DESC LIMIT 1
            ''')
        row = c.fetchone()
        conn.close()
        return row[0] if row else None
    
    def get_by_username(self, username: str) -> User:
        """
        Get a user by username
        :param username: Username
        :return: User object
        """
        conn = create_connection()
        c = conn.cursor()
        c.execute(
            '''
            SELECT * FROM user WHERE username = ?
            ''',
            (username,))
        row = c.fetchone()
        conn.close()
        return User(row[0], row[1], row[2], row[3]) if row else None